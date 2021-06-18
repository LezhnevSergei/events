from flask import jsonify, Blueprint, request
from flask.views import MethodView

from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.api.v1.constructors import Constructor
from backend.api.v1.models.events import FilterDTO
from backend.db import db
from backend.db.models import FilterModel


class FiltersModule(MethodView):
    url = "/filters"

    @jwt_required
    def get(self):
        user_id = get_jwt_identity()
        filter_models = Constructor().filters.by_user(user_id).all()
        filters = [FilterDTO.from_model(theme).dict() for theme in filter_models]

        return jsonify(filters)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        themes = Constructor().themes.ids(request.get_json().get('theme_ids')).all()
        filter = FilterModel(
            user_id=user_id,
            city_id=request.get_json().get('city_id'),
            themes=themes,
            start_at=request.get_json().get('start_at'),
            end_at=request.get_json().get('end_at'),
        )

        db.session.add(filter)
        db.session.commit()

        filter_dto = FilterDTO.from_model(filter)

        return jsonify(filter_dto.dict()), 201


def setup_modules(api: Blueprint):
    modules = (FiltersModule,)

    for module in modules:
        api.add_url_rule(module.url, view_func=module.as_view(module.__name__))
