from flask import Blueprint

from .events import setup_modules as setup_events
from .auth import setup_modules as setup_auth
from .themes import setup_modules as setup_themes
from .cities import setup_modules as setup_cities
from .filters import setup_modules as setup_filters


def setup_blueprint(api: Blueprint):
    setup_themes(api)
    setup_events(api)
    setup_auth(api)
    setup_cities(api)
    setup_filters(api)
