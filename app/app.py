# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午10:08
# @Author  : iGolden
# @Software: PyCharm
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    return app
