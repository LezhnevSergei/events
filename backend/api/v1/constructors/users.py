from __future__ import annotations
from typing import List

from sqlalchemy.orm.query import Query

from backend.db import db
from backend.db.models import UserModel


class UserQueryConstructor:
    _query: Query = None

    def __init__(self) -> None:
        self._query = db.session.query(UserModel)

    def id(self, id: int) -> UserQueryConstructor:
        self._query = self._query.filter(UserModel.id == id)
        return self

    def ids(self, ids: List[int]) -> UserQueryConstructor:
        self._query = self._query.filter(UserModel.id.in_(ids))
        return self

    def filter_email(self, email: str) -> UserQueryConstructor:
        self._query = self._query.filter(UserModel.email == email)
        return self

    def filter_login(self, login: str) -> UserQueryConstructor:
        if "@" in login:
            return self.filter_email(login)

        self._query = self._query.filter(UserModel.login == login)
        return self

    def count(self) -> int:
        return self._query.count()

    def first(self) -> UserModel:
        return self._query.first()

    def all(self) -> List[UserModel]:
        return self._query.all()
