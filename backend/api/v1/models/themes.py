from pydantic.main import BaseModel

from backend.db.models import ThemeModel


class ThemeDTO(BaseModel):
    @classmethod
    def from_model(cls, theme: ThemeModel):
        return cls(
            id=theme.id,
            name=theme.name,
            alias=theme.alias,
        )

    id: int
    name: str
    alias: str
