from flask import Blueprint

from .events import setup_modules as setup_events


def setup_blueprint(api: Blueprint):
    setup_events(api)
