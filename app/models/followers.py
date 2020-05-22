# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 上午12:59
# @Author  : iGolden
# @Software: PyCharm
from flask import g
from sqlalchemy import Column, Integer, ForeignKey, String, orm
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.models.user import User


class Followers(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    follower_id = Column(Integer)
    remark = Column(String(64), default='')

    @orm.reconstructor
    def __init__(self):
        super(Followers, self).__init__()
        self.fields = ['id', 'user_id', 'user', 'follower_id', 'remark']

    @staticmethod
    def save_followers(follower_id):
        with db.auto_commit():
            follower = Followers()
            follower.user_id = g.user.uid
            follower.follower_id = follower_id
            db.session.add(follower)

    @classmethod
    def user_followers(cls, user_id):
        followers_list = Followers.query.filter_by(user_id=user_id).all()
        followers_list = [cls.find_follower(follower) for follower in followers_list]
        return followers_list

    @classmethod
    def user_fans(cls, user_id):
        fans_list = Followers.query.filter_by(follower_id=user_id).all()
        return fans_list

    @classmethod
    def find_follower(self, follower):
        user = User.query.filter_original(id=follower.follower_id).first()
        follower.user.id = user.id
        follower.user.email = user.email
        follower.user.avatar = user.avatar
        follower.user.sex = user.sex
        follower.user.nickname = user.nickname
        follower.user.status = user.status
        return follower
