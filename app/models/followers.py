# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 上午12:59
# @Author  : iGolden
# @Software: PyCharm
from flask import g
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import Base, db


class Followers(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    follower_id = Column(Integer)
    remark = Column(String(64), default='')

    @staticmethod
    def save_followers(follower_id):
        with db.auto_commit():
            follower = Followers()
            follower.user_id = g.user.uid
            follower.follower_id = follower_id
            db.session.add(follower)
