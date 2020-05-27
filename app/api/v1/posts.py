# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 下午4:11
# @Author  : iGolden
# @Software: PyCharm
import json
import random

from flask import request, g, jsonify

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.posts import Posts
from app.validators.forms import PostsForm, PostIdForm
from app.view_model.posts import PostsCollection, PostsModel

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
    post = Posts.query.filter_original(id=id).first_or_404()
    post = PostsModel(post)
    return json.dumps(post.data)


@api.route('/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_posts(id):
    with db.auto_commit():
        posts = Posts.query.filter_original(id=id).first_or_404()
        posts.delete()
    return DeleteSuccess(msg='随记已删除！')


@api.route('/recommend', methods=['GET'])
@auth.login_required
def recommend_posts():
    posts_list = Posts.recommend()
    list = PostsCollection(posts_list)
    random.shuffle(list.data)
    return json.dumps(list.data)


@api.route('/nearby', methods=['GET'])
@auth.login_required
def nearby_posts():
    address = request.args.get('address')
    posts_list = Posts.nearby(address)
    list = PostsCollection(posts_list)
    return json.dumps(list.data)


@api.route('/search', methods=['GET'])
@auth.login_required
def search_posts():
    title = request.args.get('title')
    posts_list = Posts.search(title)
    list = PostsCollection(posts_list)
    return json.dumps(list.data)


@api.route('/address', methods=['GET'])
@auth.login_required
def address_posts():
    address = request.args.get('address')
    posts_list = Posts.address(address)
    list = PostsCollection(posts_list)
    return json.dumps(list.data)


@api.route('/user', methods=['GET'])
@auth.login_required
def user_posts():
    uid = g.user.uid
    user_id = request.args.get('uid')
    user_id = user_id if user_id is not None else uid
    posts_list = Posts.user_posts(user_id)
    list = PostsCollection(posts_list)
    return json.dumps(list.data)


@api.route('/list', methods=['GET'])
@auth.login_required
def super_posts_list():
    posts_list = Posts.super_posts_list()
    return jsonify(posts_list)


@api.route('/del', methods=['DELETE'])
@auth.login_required
def super_delete_posts():
    form = PostIdForm().validate_for_api()
    with db.auto_commit():
        posts = Posts.query.filter_original(id=form.post_id.data).first_or_404()
        posts.delete()
    return DeleteSuccess(msg='随记已删除！')
