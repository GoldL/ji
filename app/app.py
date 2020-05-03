# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午10:08
# @Author  : iGolden
# @Software: PyCharm
from flask import Flask


def register_blueprints(app):
    from app.api.vi import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    register_blueprints(app)

    return app
