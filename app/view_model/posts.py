# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 上午12:29
# @Author  : iGolden
# @Software: PyCharm
from app.models.likes import Likes


class PostsModel:
    def __init__(self, posts):
        self.id = posts['id']
        self.title = posts['title']
        self.content = posts['content']
        self.images = posts['images']
        self.location = posts['location']
        self.create_time = posts['create_time']
        self.user = posts['user']

    @property
    def like_nums(self):
        return Likes.query.filter_by(post_id=self.id).count()


class PostsCollection:
    def __init__(self):
        self.list = []

    def fill(self, posts_list):
        self.list = [PostsModel(posts) for posts in posts_list]
