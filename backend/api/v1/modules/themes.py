from flask import request, jsonify, Blueprint
from flask.views import MethodView

from flask_jwt_extended import jwt_required

from backend.api.v1.constructors import Constructor
from backend.api.v1.models.themes import ThemeDTO


class ThemesModule(MethodView):
    url = "/themes"

    @jwt_required
    def get(self, *args, **kwargs):
        themes = Constructor().themes.all()
        dtos = [ThemeDTO.from_model(theme).json() for theme in themes]

        return jsonify(dtos)


def setup_modules(api: Blueprint):
    modules = (ThemesModule,)

    for module in modules:
        api.add_url_rule(module.url, view_func=module.as_view(module.__name__))
