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
        followers_list = Followers.query.filter_by(user_id=user_id).join(User, User.id == Followers.follower_id).all()
        return followers_list

    @classmethod
    def user_fans(cls, user_id):
        fans_list = Followers.query.filter_by(follower_id=user_id).all()
        return fans_list
