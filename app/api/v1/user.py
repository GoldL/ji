# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午10:48
# @Author  : iGolden
# @Software: PyCharm
from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/get')
def get_user():
    return 'get user'
