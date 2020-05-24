# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 上午12:53
# @Author  : iGolden
# @Software: PyCharm
from flask import jsonify

from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.comments import Comments
from app.validators.forms import CommentsForm, PostIdForm

api = Redprint('comments')


@api.route('/save', methods=['POST'])
@auth.login_required
def save_posts():
    form = CommentsForm().validate_for_api()
    Comments.save_comments(form.post_id.data, form.content.data)
    return Success(msg='评论创建成功！')


@api.route('/posts', methods=['POST'])
@auth.login_required
def posts_comments():
    form = PostIdForm().validate_for_api()
    list = Comments.posts_comments(form.post_id.data)
    return jsonify(list)


@api.route('/my', methods=['GET'])
@auth.login_required
def my_comments():
    list = Comments.my_comments()
    return jsonify(list)


@api.route('/received', methods=['GET'])
@auth.login_required
def received_comments():
    list = Comments.received_comments()
    return jsonify(list)