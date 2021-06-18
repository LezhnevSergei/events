import enum
import json
from datetime import datetime, date

from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from backend.api.v1 import api as v1
from backend.db import db
from backend.db.halpers import config_base
from backend.db.models import ThemeModel, CityModel


class FlaskEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, enum.Enum):
            return obj.name
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%dT%H:%MZ")
        if isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        return json.JSONEncoder.default(self, obj)


app = Flask(__name__)
app.url_map.strict_slashes = False
app.json_encoder = FlaskEncoder
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://sergei:123123@localhost:5432/events"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_BLACKLIST_ENABLED"] = False
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 3600
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = 86400
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access", "refresh"]
app.config["JWT_SECRET_KEY"] = "very secret"

jwt = JWTManager(app)

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all(app=app)
    config_base(db)

app.register_blueprint(v1, url_prefix="/api/v1")

if __name__ == '__main__':
    app.run(debug=True)
