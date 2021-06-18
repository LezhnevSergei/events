from __future__ import annotations
from typing import List

from sqlalchemy.orm.query import Query

from backend.db import db
from backend.db.models import CityModel


class CityQueryConstructor:
    _query: Query = None

    def __init__(self) -> None:
        self._query = db.session.query(CityModel)

    def id(self, id: int) -> CityQueryConstructor:
        self._query = self._query.filter(CityModel.id == id)
        return self

    def ids(self, ids: List[int]) -> CityQueryConstructor:
        self._query = self._query.filter(CityModel.id.in_(ids))
        return self

    def count(self) -> int:
        return self._query.count()

    def first(self) -> CityModel:
        return self._query.first()

    def all(self) -> List[CityModel]:
        return self._query.all()
