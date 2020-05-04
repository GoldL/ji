# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午10:48
# @Author  : iGolden
# @Software: PyCharm
from flask import jsonify

from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)
