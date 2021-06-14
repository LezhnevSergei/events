from datetime import datetime
from typing import List, Optional

from pydantic.main import BaseModel

from backend.api.v1.models.themes import ThemeDTO
from backend.db.models import EventModel, CityModel


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

        try:
            start = datetime.strptime(query_params.get('start', ''), '%d-%m-%Y %H:%M:%S')
            end = datetime.strptime(query_params.get('end', ''), '%d-%m-%Y %H:%M:%S')
        except ValueError:
            start = None
            end = None

        return cls(
            limit=query_params.get('limit'),
            offset=query_params.get('offset'),
            start=start,
            end=end,
            theme_id=query_params.get('theme_id'),
            city_id=query_params.get('city_id')
        )

    start: Optional[datetime]
    end: Optional[datetime]
    theme_id: Optional[int]
    city_id: Optional[int]
    limit: Optional[int]
    offset: Optional[int]


class EventListMetaDTO(BaseModel):
    amount: int


class EventListDTO(BaseModel):
    meta: EventListMetaDTO
    items: List[EventDTO]
