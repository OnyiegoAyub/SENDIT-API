

"""Instance of Flask application"""

from instance.config import Config
from flask import Flask, Blueprint, make_response, jsonify
from .api.v1 import blueprint_version1


def page_not_found(e):
  return make_response(jsonify(
                {
                    "Message": "url given not available in this server"
                }), 404)


def create_app(config_class=Config):
    """"initialize app method"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(blueprint_version1, url_prefix='/api/v1')
    app.register_error_handler(404, page_not_found)

    return app
