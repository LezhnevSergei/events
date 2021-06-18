from __future__ import annotations
from typing import List

from sqlalchemy.orm.query import Query

from backend.db import db
from backend.db.models import FilterModel


class FilterQueryConstructor:
    _query: Query = None

    def __init__(self) -> None:
        self._query = db.session.query(FilterModel)

    def id(self, id: int) -> FilterQueryConstructor:
        self._query = self._query.filter(FilterModel.id == id)
        return self

    def ids(self, ids: List[int]) -> FilterQueryConstructor:
        self._query = self._query.filter(FilterModel.id.in_(ids))
        return self

    def by_user(self, user_id: int) -> FilterQueryConstructor:
        self._query = self._query.filter(FilterModel.user_id == user_id)
        return self

    def count(self) -> int:
        return self._query.count()

    def first(self) -> FilterModel:
        return self._query.first()

    def all(self) -> List[FilterModel]:
        return self._query.all()
