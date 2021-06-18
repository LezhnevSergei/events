from flask import jsonify, Blueprint
from flask.views import MethodView

from flask_jwt_extended import jwt_required

from backend.api.v1.constructors import Constructor
from backend.api.v1.models.events import CityDTO


class CitiesModule(MethodView):
    url = "/cities"

    @jwt_required
    def get(self):
        city_models = Constructor().cities.all()
        events = [CityDTO.from_model(city).dict() for city in city_models]

        return jsonify(events)


def setup_modules(api: Blueprint):
    modules = (CitiesModule,)

    for module in modules:
        api.add_url_rule(module.url, view_func=module.as_view(module.__name__))
