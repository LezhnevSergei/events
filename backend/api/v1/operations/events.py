from typing import List, Tuple, Optional

from backend.api.v1.constructors import Constructor, EventQueryConstructor
from backend.api.v1.models.events import EventFilterDTO, EventListDTO, EventDTO, EventListMetaDTO, EventCreateDTO
from backend.db import db
from backend.db.models import EventModel, ThemeModel


def get_events(filters: Optional[EventFilterDTO] = None) -> List[EventModel]:
    events = Constructor().events

    if filters is not None:
        events = _get_filtered_events(events=events, filters=filters)

    events = events.order_by_date().all()

    return events


def create_event(event_input: EventCreateDTO, creator_id: int) -> EventModel:
    themes = db.session.query(ThemeModel).filter(ThemeModel.id.in_(event_input.theme_ids)).all()

    new_event = EventModel(
        name=event_input.name,
        start_at=event_input.start_at,
        end_at=event_input.end_at,
        city_id=event_input.city_id,
        creator_id=creator_id,
        themes=themes,
    )
    db.session.add(new_event)
    db.session.commit()

    return new_event


def get_event(event_id) -> EventModel:
    event = db.session.query(EventModel).get(event_id)
    return event


def delete_event(event_id) -> None:
    event = get_event(event_id)
    db.session.delete(event)
    db.session.commit()


def _get_filtered_events(events: EventQueryConstructor, filters):
    if filters.theme_ids:
        events = events.filter_theme(filters.theme_ids)
    if filters.city_id:
        events = events.filter_city(filters.city_id)
    if filters.start or filters.end:
        events = events.filter_dates(start=filters.start, end=filters.end)
    if filters.limit or filters.offset:
        events = events.restrict(limit=filters.limit, offset=filters.offset)

    return events
