# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 上午12:29
# @Author  : iGolden
# @Software: PyCharm
from flask import g, jsonify

from app.models.collections import Collections
from app.models.likes import Likes


class PostsCollection:
    def __init__(self, posts):
        self.data = []
        self.data = self._parse(posts)

    def _parse(self, posts):
        return [PostsModel(post).data for post in posts]


class PostsModel:
    def __init__(self, post):
        self.data = {}
        self.data = self._parse(post)

    def _parse(self, post):
        user_id = g.user.uid
        like_num = Likes.query.filter_by(post_id=post.id).count()
        is_like = False
        like = Likes.query.filter_by(post_id=post.id, user_id=user_id).first()
        if like:
            is_like = True
        is_collection = False
        collection = Collections.query.filter_by(post_id=post.id, user_id=user_id).first()
        if collection:
            is_collection = True
        r = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'images': post.images,
            'location': post.location,
            'create_time': post.create_time,
            'user_id': post.user.id,
            'user_avatar': post.user.avatar,
            'user_sex': post.user.sex,
            'user_nickname': post.user.nickname,
            'like_num': like_num,
            'is_like': is_like,
            'is_collection': is_collection
        }

        return r
