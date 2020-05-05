# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 下午3:47
# @Author  : iGolden
# @Software: PyCharm
from flask import g
from sqlalchemy import Column, Integer, ForeignKey, orm, String, Text
from sqlalchemy.orm import relationship

from app.models.base import Base, db


class Posts(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    title = Column(String(128))
    content = Column(Text)
    images = Column(String(255))
    location = Column(String(128))

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'user_id', 'title', 'content', 'images', 'location']

    @staticmethod
    def save_posts(title, content, images, location):
        with db.auto_commit():
            posts = Posts()
            posts.user_id = g.user.uid
            posts.title = title
            posts.content = content
            posts.images = images
            posts.location = location
            db.session.add(posts)
