# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 下午4:11
# @Author  : iGolden
# @Software: PyCharm
from flask import jsonify

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.likes import Likes
from app.models.posts import Posts
from app.models.user import User
from app.validators.forms import PostsForm

api = Redprint('posts')


@api.route('/save', methods=['POST'])
@auth.login_required
def save_posts():
    form = PostsForm().validate_for_api()
    Posts.save_posts(form.title.data, form.content.data, form.images.data, form.location.data)
    return Success(msg='随记创建成功！')


@api.route('/<int:id>', methods=['GET'])
@auth.login_required
def get_posts(id):
    posts = Posts.query.filter_by(id=id).first_or_404()
    return jsonify(posts)


@api.route('/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_posts(id):
    with db.auto_commit():
        posts = Posts.query.filter_by(id=id).first_or_404()
        posts.delete()
    return DeleteSuccess(msg='随记已删除！')


@api.route('/recommend', methods=['GET'])
@auth.login_required
def recommend_posts():
    posts_list = Posts.query.filter_by().join(User, User.id == Posts.user_id).all()
    return jsonify(posts_list)
