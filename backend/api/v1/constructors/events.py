from __future__ import annotations

from datetime import datetime
from typing import List

from sqlalchemy.orm.query import Query

from backend.db import db
from backend.db.models import EventModel, ThemeModel


class EventQueryConstructor:
    _query: Query = None

    def __init__(self) -> None:
        self._query = db.session.query(EventModel)

    def id(self, id: int) -> EventQueryConstructor:
        self._query = self._query.filter(EventModel.id == id)
        return self

    def ids(self, ids: List[int]) -> EventQueryConstructor:
        self._query = self._query.filter(EventModel.id.in_(ids))
        return self

    def filter_city(self, city_id: int) -> EventQueryConstructor:
        self._query = self._query.filter(EventModel.city_id == city_id)
        return self

    def filter_theme(self, theme_id: int) -> EventQueryConstructor:
        self._query = self._query.filter(EventModel.themes.any(ThemeModel.id == theme_id))
        return self

    def filter_dates(self, start: datetime, end: datetime) -> EventQueryConstructor:
        if start:
            self._query = self._query.filter(EventModel.end_at > start)
        if end:
            self._query = self._query.filter(EventModel.end_at < end)
        return self

    def order_by_date(self) -> EventQueryConstructor:
        self._query = self._query.order_by(EventModel.created_at.desc())
        return self

    def restrict(self, limit: int = None, offset: int = None) -> EventQueryConstructor:
        if limit:
            self._query = self._query.limit(limit)
        if offset:
            self._query = self._query.offset(offset)
        return self

    def count(self) -> int:
        return self._query.count()

    def first(self) -> EventModel:
        return self._query.first()

    def all(self) -> List[EventModel]:
        return self._query.all()
