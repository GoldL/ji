# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 下午11:55
# @Author  : iGolden
# @Software: PyCharm
from flask import g
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, db


class Likes(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    posts = relationship('Posts')
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

    @staticmethod
    def save_likes(post_id):
        with db.auto_commit():
            likes = Likes()
            likes.user_id = g.user.uid
            likes.post_id = post_id
            db.session.add(likes)
