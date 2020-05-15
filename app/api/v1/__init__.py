# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午10:51
# @Author  : iGolden
# @Software: PyCharm
from flask import Blueprint

from app.api.v1 import user
from app.api.v1 import client
from app.api.v1 import token
from app.api.v1 import posts
from app.api.v1 import reports
from app.api.v1 import likes
from app.api.v1 import collections
from app.api.v1 import followers


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)
    posts.api.register(bp_v1)
    reports.api.register(bp_v1)
    likes.api.register(bp_v1)
    collections.api.register(bp_v1)
    followers.api.register(bp_v1)

    return bp_v1
