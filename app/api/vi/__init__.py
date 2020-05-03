# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午10:51
# @Author  : iGolden
# @Software: PyCharm
from flask import Blueprint

from app.api.vi import user


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    return bp_v1
