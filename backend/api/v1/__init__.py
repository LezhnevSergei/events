from flask import Blueprint, request, jsonify
from flask_cors import CORS

from .modules import setup_blueprint


api = Blueprint("v1", __name__)
cors = CORS(api, supports_credentials=True)


@api.before_request
def before_api_request():
    if request.method in ["GET", "OPTIONS", "DELETE"]:
        return None
    if not request.is_json or request.json is None:
        return jsonify(error="msg payload incorrect"), 400
    return None


setup_blueprint(api)
