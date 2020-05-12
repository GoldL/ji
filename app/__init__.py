# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 上午8:46
# @Author  : iGolden
# @Software: PyCharm
from .app import Flask
from flask_cors import CORS


def register_blueprints(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def apply_cors(app):
    CORS(app,  resources={r"/*": {"origins": "*"}})


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    register_blueprints(app)
    register_plugin(app)

    apply_cors(app)

    return app
