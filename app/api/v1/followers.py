# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 上午1:20
# @Author  : iGolden
# @Software: PyCharm
from flask import g

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
    follower = Followers.query.filter_original(follower_id=form.user_id.data).first()
    if not follower:
        Followers.save_followers(form.user_id.data)
    else:
        user_id = g.user.uid
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
