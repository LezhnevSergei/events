from .cities import CityQueryConstructor
from .events import EventQueryConstructor
from .theme import ThemeQueryConstructor
from .users import UserQueryConstructor


class Constructor:
    @property
    def users(cls) -> UserQueryConstructor:
        return UserQueryConstructor()

    @property
    def events(cls) -> EventQueryConstructor:
        return EventQueryConstructor()

    @property
    def themes(cls) -> ThemeQueryConstructor:
        return ThemeQueryConstructor()

    @property
    def cities(cls) -> CityQueryConstructor:
        return CityQueryConstructor()
