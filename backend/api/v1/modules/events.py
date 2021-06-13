from flask import request, jsonify, Blueprint
from flask.views import MethodView

from backend.db import db
from backend.db.models import EventModel, UserModel, ThemeModel


class EventsModule(MethodView):
    url = "/events"

    def get(self, *args, **kwargs):
        return jsonify("Events")


def setup_modules(api: Blueprint):
    modules = (EventsModule,)

    for module in modules:
        api.add_url_rule(module.url, view_func=module.as_view(module.__name__))
