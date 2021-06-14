from flask import request, jsonify, Blueprint
from flask.views import MethodView
from flask_jwt_extended import (
    jwt_refresh_token_required,
    create_access_token,
    get_jwt_identity,
    get_raw_jwt,
    jwt_required,
)

from backend.db import db
from ..constructors import Constructor
from ..models.auth import (
    AuthIdentityDTO,
    LoginInputDTO,
    AuthDataDTO,
    RegistrationInputDTO,
)
from ..operations.auth import (
    op_register,
    op_logout,
)


class AuthLoginModule(MethodView):
    url = "/auth/login"

    def post(self, *args, **kwargs):
        model = LoginInputDTO(**request.get_json())

        user = Constructor().users.filter_login(model.login).first()
        if user is None or not user.verify_password(model.password):
            raise Exception("Пользователь не найден или неправильный пароль")

        dto = AuthDataDTO.from_model(user)
        return jsonify(dto.dict())


class AuthLogoutModule(MethodView):
    url = "/auth/logout"

    @jwt_refresh_token_required
    def post(self, *args, **kwargs):
        jti = get_raw_jwt()["jti"]
        op_logout(jti)

        return jsonify(status="success")


class AuthMeModule(MethodView):
    url = "/auth/me"

    @jwt_required
    def get(self, *args, **kwargs):
        user_id = get_jwt_identity()
        user = Constructor().users.id(user_id).first()

        dto = AuthIdentityDTO.from_model(user)
        return jsonify(dto.dict())


class AuthRegisterModule(MethodView):
    url = "/auth/register"

    def post(self, *args, **kwargs):
        model = RegistrationInputDTO(**request.get_json())

        user = Constructor().users.filter_login(model.login).first()
        if user is not None:
            raise Exception("Пользователь с таким логином уже существует")
        if model.email is not None:
            user = Constructor().users.filter_email(model.email).first()
            if user is not None:
                raise Exception("Пользователь с такой почтой уже существует")

        user = op_register(model)

        db.session.add(user)
        db.session.commit()

        dto = AuthIdentityDTO.from_model(user)

        return jsonify(dto.dict())


class AuthRefreshModule(MethodView):
    url = "/auth/refresh"

    @jwt_refresh_token_required
    def get(self, *args, **kwargs):
        token = create_access_token(
            get_jwt_identity(),
        )

        return jsonify(access_token=token)


def setup_modules(api: Blueprint):
    modules = {
        AuthMeModule,
        AuthLoginModule,
        AuthLogoutModule,
        AuthRefreshModule,
        AuthRegisterModule,
    }

    for module in modules:
        api.add_url_rule(module.url, view_func=module.as_view(module.__name__))
