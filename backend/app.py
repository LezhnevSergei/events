from flask import Flask
from flask_migrate import Migrate

from backend.api.v1 import api as v1
from backend.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://sergei:123123@localhost:5432/events"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

db.create_all(app=app)

app.register_blueprint(v1, url_prefix="/api/v1")


if __name__ == '__main__':
    app.run(debug=True)
