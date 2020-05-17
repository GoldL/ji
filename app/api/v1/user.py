# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午10:48
# @Author  : iGolden
# @Software: PyCharm
import json

from flask import jsonify, g, request

from app.libs.error_code import DeleteSuccess, Success
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User
from app.validators.forms import UserIdForm, UserUpdateForm
from app.view_model.user import UserModel

api = Redprint('user')


@api.route('/list', methods=['GET'])
@auth.login_required
def super_user_list():
    list = User.user_list()
    return jsonify(list)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/del', methods=['DELETE'])
@auth.login_required
def super_delete_user():
    with db.auto_commit():
        form = UserIdForm().validate_for_api()
        user = User.query.filter_by(id=form.user_id.data).first_or_404()
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


@api.route('/update', methods=['POST'])
@auth.login_required
def update_user():
    form = UserUpdateForm().validate_for_api()
    user_id = g.user.uid
    with db.auto_commit():
        User.query.filter_by(id=user_id).update({
            User.nickname: form.nickname.data,
            User.avatar: form.avatar.data,
            User.sex: form.sex.data
        })
    user = User.query.filter_by(id=user_id).first()
    user = UserModel(user)
    return json.dumps(user.data)


@api.route('/active', methods=['POST'])
@auth.login_required
def active_user():
    form = UserIdForm().validate_for_api()
    with db.auto_commit():
        User.query.filter_original(id=form.user_id.data).update({User.status: 1})
    return Success(msg='用户已恢复！')
