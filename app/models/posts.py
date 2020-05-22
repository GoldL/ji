# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 下午3:47
# @Author  : iGolden
# @Software: PyCharm
from flask import g, current_app
from sqlalchemy import Column, Integer, ForeignKey, orm, String, Text
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.models.user import User


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
        super(Posts, self).__init__()
        self.fields = ['id', 'user_id', 'title', 'content', 'images', 'location', 'create_datetime', 'user', 'status']

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

    @classmethod
    def recommend(cls):
        posts_list = Posts.query.filter_by().all()
        return posts_list

    @classmethod
    def nearby(cls):
        posts_list = Posts.query.filter_by().all()
        return posts_list

    @classmethod
    def search(cls, title):
        posts_list = Posts.query.filter(
            Posts.title.like("%" + title + "%") if title is not None else "",
            Posts.status == 1
        ).limit(current_app.config('PAGE_POSTS_COUNT')).all()
        return posts_list

    @classmethod
    def address(cls, address):
        posts_list = Posts.query.filter(
            Posts.location.like("%" + address + "%") if address is not None else "",
            Posts.status == 1
        ).limit(current_app.config('PAGE_POSTS_COUNT')).all()
        return posts_list

    @classmethod
    def user_posts(cls, user_id):
        posts_list = Posts.query.filter_by(user_id=user_id).join(User, User.id == Posts.user_id).all()
        return posts_list

    @classmethod
    def super_posts_list(cls):
        posts_list = Posts.query.filter_by().join(User, User.id == Posts.user_id).all()
        return posts_list
