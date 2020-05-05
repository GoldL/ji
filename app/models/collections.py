# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 上午12:04
# @Author  : iGolden
# @Software: PyCharm
from flask import g
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import Base, db


class Collections(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    posts = relationship('Posts')
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)

    @staticmethod
    def save_collections(post_id):
        with db.auto_commit():
            collections = Collections()
            collections.user_id = g.user.uid
            collections.post_id = post_id
            db.session.add(collections)
