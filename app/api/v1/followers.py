# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 上午1:20
# @Author  : iGolden
# @Software: PyCharm
from flask import g, request, jsonify

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.followers import Followers
from app.validators.forms import UserIdForm

api = Redprint('followers')


@api.route('/follower', methods=['POST'])
@auth.login_required
def follower_user():
    form = UserIdForm().validate_for_api()
    user_id = g.user.uid
    follower = Followers.query.filter_original(user_id=user_id, follower_id=form.user_id.data).first()
    if not follower:
        Followers.save_followers(form.user_id.data)
    else:
        with db.auto_commit():
            Followers.query.filter_original(user_id=user_id, follower_id=form.user_id.data).update({Followers.status: 1})
    return Success(msg='关注成功！')


@api.route('/unfollower', methods=['DELETE'])
@auth.login_required
def unfollower_user():
    form = UserIdForm().validate_for_api()
    user_id = g.user.uid
    with db.auto_commit():
        follower = Followers.query.filter_original(user_id=user_id, follower_id=form.user_id.data).first_or_404()
        follower.delete()
    return DeleteSuccess(msg='取消关注')


@api.route('/user', methods=['GET'])
@auth.login_required
def user_followers():
    uid = g.user.uid
    user_id = request.args.get('uid')
    user_id = user_id if user_id is not None else uid
    followers_list = Followers.user_followers(user_id)
    return jsonify(followers_list)


@api.route('/fans', methods=['GET'])
@auth.login_required
def user_fans():
    uid = g.user.uid
    user_id = request.args.get('uid')
    user_id = user_id if user_id is not None else uid
    fans_list = Followers.user_fans(user_id)
    return jsonify(fans_list)
