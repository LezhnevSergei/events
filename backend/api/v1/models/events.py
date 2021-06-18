from datetime import datetime
from typing import List, Optional

from pydantic.main import BaseModel

from backend.api.v1.models.themes import ThemeDTO
from backend.db.models import EventModel, CityModel, FilterModel


class CityDTO(BaseModel):
    @classmethod
    def from_model(cls, city: CityModel):
        return cls(id=city.id, name=city.name, alias=city.alias)

    id: int
    name: str
    alias: str


class EventDTO(BaseModel):
    @classmethod
    def from_model(cls, event: EventModel):
        themes = [ThemeDTO.from_model(theme) for theme in event.themes]

        return cls(
            id=event.id,
            name=event.name,
            created_at=event.created_at.strftime('%d-%m-%Y %H:%M:%S'),
            start_at=event.start_at.strftime('%d-%m-%Y %H:%M:%S'),
            end_at=event.end_at.strftime('%d-%m-%Y %H:%M:%S'),
            themes=themes,
            city=CityDTO.from_model(event.city),
        )

    id: int
    name: str
    created_at: str
    start_at: str
    end_at: str
    themes: List[ThemeDTO]
    city: CityDTO


class EventCreateDTO(BaseModel):
    name: str
    start_at: str
    end_at: str
    theme_ids: List[int]
    city_id: int


class EventFilterDTO(BaseModel):
    @classmethod
    def from_query_params(cls, query_params):
        if query_params is {}:
            return None

        theme_ids = query_params.get('theme_ids')
        if theme_ids:
            theme_ids = [int(id) for id in theme_ids.split(',')]

        print(query_params.get('start', ''))

        start = None
        if query_params.get('start') is not None:
            start = datetime.strptime(query_params.get('start'), '%d-%m-%Y %H:%M:%S')

        end = None
        if query_params.get('end') is not None:
            end = datetime.strptime(query_params.get('end'), '%d-%m-%Y %H:%M:%S')

        print(start, end)

        return cls(
            limit=query_params.get('limit'),
            offset=query_params.get('offset'),
            start=start,
            end=end,
            theme_ids=theme_ids,
            city_id=query_params.get('city_id')
        )

    start: Optional[datetime]
    end: Optional[datetime]
    theme_ids: Optional[List[int]]
    city_id: Optional[int]
    limit: Optional[int]
    offset: Optional[int]


class FilterDTO(BaseModel):
    @classmethod
    def from_model(cls, filter: FilterModel):
        theme_ids = [theme.id for theme in filter.themes]

        return cls(
            id=filter.id,
            start_at=filter.start_at.strftime('%d-%m-%Y %H:%M:%S'),
            end_at=filter.end_at.strftime('%d-%m-%Y %H:%M:%S'),
            theme_ids=theme_ids,
            city_id=filter.city_id or None,
            user_id=filter.user_id or None,
        )

    id: int
    user_id: int
    city_id: int
    theme_ids: List[int]
    start_at: Optional[str]
    end_at: Optional[str]


class EventListMetaDTO(BaseModel):
    amount: int


class EventListDTO(BaseModel):
    meta: EventListMetaDTO
    items: List[EventDTO]
