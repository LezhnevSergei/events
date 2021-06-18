from flask import request, jsonify, Blueprint
from flask.views import MethodView

from flask_jwt_extended import get_jwt_identity, jwt_required

from backend.api.v1.constructors import Constructor
from backend.api.v1.models.events import EventDTO, EventCreateDTO, EventFilterDTO, EventListMetaDTO, EventListDTO
from backend.api.v1.operations.events import get_events, create_event, get_event, delete_event


class EventsModule(MethodView):
    url = "/events"

    @jwt_required
    def get(self):
        filters = EventFilterDTO.from_query_params(request.args)
        print(request.args)
        print(filters)
        filtered_events = get_events(filters)
        events_total_count = Constructor().events.count()

        events = [EventDTO.from_model(event).dict() for event in filtered_events]

        meta = EventListMetaDTO(amount=events_total_count)
        event_list = EventListDTO(meta=meta, items=events).json()

        return jsonify(event_list)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        event_input = EventCreateDTO(**request.get_json())

        new_event = create_event(event_input=event_input, creator_id=user_id)

        event = EventDTO.from_model(new_event)

        return jsonify(event.json()), 201


class EventModule(MethodView):
    url = "/events/<int:event_id>"

    @jwt_required
    def get(self, event_id: int):
        event = get_event(event_id)
        events_dto = EventDTO.from_model(event)

        return jsonify(events_dto.json())

    @jwt_required
    def delete(self, event_id: int):
        delete_event(event_id)

        return jsonify(), 204


def setup_modules(api: Blueprint):
    modules = (EventsModule, EventModule)

    for module in modules:
        api.add_url_rule(module.url, view_func=module.as_view(module.__name__))
