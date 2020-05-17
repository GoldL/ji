# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 上午12:07
# @Author  : iGolden
# @Software: PyCharm
from flask import g, request, jsonify

from app.libs.error_code import Success, DeleteSuccess
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.collections import Collections
from app.validators.forms import PostIdForm

api = Redprint('collections')


@api.route('/collection', methods=['POST'])
@auth.login_required
def collection_posts():
    form = PostIdForm().validate_for_api()
    user_id = g.user.uid
    collections = Collections.query.filter_original(user_id=user_id, post_id=form.post_id.data).first()
    if not collections:
        Collections.save_collections(form.post_id.data)
    else:
        Collections.query.filter_original(user_id=user_id, post_id=form.post_id.data).update({Collections.status: 1})
    return Success(msg='添加至收藏！')


@api.route('/uncollection', methods=['DELETE'])
@auth.login_required
def uncollection_posts():
    form = PostIdForm().validate_for_api()
    user_id = g.user.uid
    with db.auto_commit():
        collections = Collections.query.filter_original(user_id=user_id, post_id=form.post_id.data).first_or_404()
        collections.delete()
    return DeleteSuccess(msg='取消收藏')


@api.route('/user', methods=['GET'])
@auth.login_required
def user_collection():
    uid = g.user.uid
    user_id = request.args.get('uid')
    user_id = user_id if user_id is not None else uid
    collection_list = Collections.user_collection(user_id)
    return jsonify(collection_list)
