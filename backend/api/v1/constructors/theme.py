from __future__ import annotations
from typing import List

from sqlalchemy.orm.query import Query

from backend.db import db
from backend.db.models import ThemeModel


class ThemeQueryConstructor:
    _query: Query = None

    def __init__(self) -> None:
        self._query = db.session.query(ThemeModel)

    def id(self, id: int) -> ThemeQueryConstructor:
        self._query = self._query.filter(ThemeModel.id == id)
        return self

    def ids(self, ids: List[int]) -> ThemeQueryConstructor:
        self._query = self._query.filter(ThemeModel.id.in_(ids))
        return self

    def count(self) -> int:
        return self._query.count()

    def first(self) -> ThemeModel:
        return self._query.first()

    def all(self) -> List[ThemeModel]:
        return self._query.all()
