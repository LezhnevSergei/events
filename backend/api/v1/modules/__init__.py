from flask import Blueprint

from .events import setup_modules as setup_events
from .auth import setup_modules as setup_auth
from .themes import setup_modules as setup_themes


def setup_blueprint(api: Blueprint):
    setup_themes(api)
    setup_events(api)
    setup_auth(api)
