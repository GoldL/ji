# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午10:48
# @Author  : iGolden
# @Software: PyCharm
import json

from flask import jsonify, g, request

from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User
from app.validators.forms import UserIdForm
from app.view_model.user import UserModel

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user_id = request.args.get('uid')
    user_id = user_id if user_id is not None else uid
    user = User.query.filter_by(id=user_id).first_or_404()
    user = UserModel(user)
    return json.dumps(user.data)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('', methods=['POST'])
@auth.login_required
def get_other_user():
    form = UserIdForm().validate_for_api()
    user = User.query.filter_by(id=form.user_id.data).first_or_404()
    user = UserModel(user)
    return json.dumps(user.data)
