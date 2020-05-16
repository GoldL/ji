# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 上午12:07
# @Author  : iGolden
# @Software: PyCharm
from flask import g

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.likes import Likes
from app.validators.forms import PostIdForm

api = Redprint('likes')


@api.route('/like', methods=['POST'])
@auth.login_required
def like_posts():
    form = PostIdForm().validate_for_api()
    like = Likes.query.filter_original(post_id=form.post_id.data).first()
    if not like:
        Likes.save_likes(form.post_id.data)
    else:
        user_id = g.user.uid
        Likes.query.filter_original(user_id=user_id, post_id=form.post_id.data).update({Likes.status: 1})
    return Success(msg='添加至喜欢！')


@api.route('/unlike', methods=['DELETE'])
@auth.login_required
def unlike_posts():
    form = PostIdForm().validate_for_api()
    user_id = g.user.uid
    with db.auto_commit():
        like = Likes.query.filter_original(user_id=user_id, post_id=form.post_id.data).first_or_404()
        like.delete()
    return DeleteSuccess(msg='取消喜欢')
