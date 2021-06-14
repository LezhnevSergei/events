from itertools import groupby
from datetime import datetime, timedelta

from backend.db import db
from backend.db.models import UserModel
from ..models.auth import RegistrationInputDTO, ResetInputDTO


def op_register(model: RegistrationInputDTO):
    user = UserModel(
        login=model.login,
        email=model.email,
    )
    user.set_password(model.password)

    db.session.add(user)
    db.session.commit()

    return user


def op_logout(jti: str):
    expire = datetime.now() + timedelta(days=30)
    # token = dbm.RevokedTokenModel(jti=jti, expire_at=expire)

    # db.session.add(token)
    db.session.commit()


# def op_reset_password(model: ResetInputDTO):
#     srv: TokenService = ServiceBroker.retrieve("Token")
#     token = srv.get_token(TokenEnum.reset, model.login)
#
#     if token is None or token != model.token:
#         raise ApiDataException("Токен не существует", "CODE_FAILED")
#
#     user = Constructor().users.filter_login(model.login).first()
#     user.set_password(model.password)
#
#     srv.delete_token(TokenEnum.reset, model.login)
#
#     db.session.add(user)
#     db.session.commit()
