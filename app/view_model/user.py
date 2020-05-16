# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 上午12:39
# @Author  : iGolden
# @Software: PyCharm

from app.models.collections import Collections
from app.models.followers import Followers
from app.models.posts import Posts


class UserCollection:
    def __init__(self, users):
        self.data = []
        self.data = self._parse(users)

    def _parse(self, users):
        return [UserModel(user).data for user in users]


class UserModel:
    def __init__(self, user):
        self.data = {}
        self.data = self._parse(user)

    def _parse(self, user):
        posts_num = Posts.query.filter_by(user_id=user.id).count()
        follower_num = Followers.query.filter_by(user_id=user.id).count()
        collection_num = Collections.query.filter_by(user_id=user.id).count()
        fans_num = Followers.query.filter_by(follower_id=user.id).count()

        r = {
            'id': user.id,
            'avatar': user.avatar,
            'sex': user.sex,
            'email': user.email,
            'nickname': user.nickname,
            'posts_num': posts_num,
            'follower_num': follower_num,
            'collection_num': collection_num,
            'fans_num': fans_num
        }
        
        return r
