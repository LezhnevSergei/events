import bcrypt
from sqlalchemy.sql import func

from backend.db import db

themes = db.Table(
    'event_themes',
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True),
    db.Column('theme_id', db.Integer, db.ForeignKey('themes.id'), primary_key=True)
)


class EventModel(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    creator_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    start_at = db.Column(db.DateTime, nullable=False)
    end_at = db.Column(db.DateTime, nullable=False)
    city_id = db.Column(db.BigInteger, db.ForeignKey('cities.id'), nullable=False)

    creator = db.relationship('UserModel', backref=db.backref('event', lazy=True))

    themes = db.relationship(
        'ThemeModel',
        secondary=themes,
        lazy='subquery',
        backref=db.backref('event', lazy=True)
    )

    city = db.relationship(
        "CityModel",
        uselist=False,
        lazy="joined",
    )


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    login = db.Column(db.String, index=True, unique=False, nullable=True)
    email = db.Column(db.String, index=True, unique=True, nullable=True)
    passhash = db.Column(db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())

    def set_password(self, password):
        if isinstance(password, str):
            password = password.encode('utf-8')
        self.passhash = str(bcrypt.hashpw(password, bcrypt.gensalt()), 'utf8')

    def verify_password(self, password):
        if self.passhash is None:
            return False
        if isinstance(password, str):
            password = password.encode('utf-8')
        return bcrypt.checkpw(password, self.passhash.encode('utf-8'))


class ThemeModel(db.Model):
    __tablename__ = 'themes'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    alias = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)


class CityModel(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    alias = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
