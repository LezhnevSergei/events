from backend.db.models import ThemeModel, CityModel


def config_base(db):
    if (
            db.session.query(ThemeModel).filter(ThemeModel.alias == "prog").first()
            is None
    ):
        theme_prog = ThemeModel(name="Programming", alias="prog")
        db.session.add(theme_prog)

    if (
            db.session.query(ThemeModel).filter(ThemeModel.alias == "travel").first()
            is None
    ):
        theme_travel = ThemeModel(name="Travelling", alias="travel")
        db.session.add(theme_travel)

    if (
            db.session.query(CityModel).filter(CityModel.alias == "msc").first()
            is None
    ):
        city_msc = CityModel(name="Moscow", alias="msc")
        db.session.add(city_msc)

    if (
            db.session.query(CityModel).filter(CityModel.alias == "spb").first()
            is None
    ):
        city_spb = CityModel(name="Saint Petersburg", alias="spb")
        db.session.add(city_spb)

    db.session.commit()
