# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 上午12:46
# @Author  : iGolden
# @Software: PyCharm
from flask import g, current_app
from sqlalchemy import Column, Integer, ForeignKey, orm, String
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.models.posts import Posts


class Comments(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    posts = relationship('Posts')
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=False)
    content = Column(String(128))

    @orm.reconstructor
    def __init__(self):
        super(Comments, self).__init__()
        self.fields = ['id', 'user_id', 'content', 'post_id', 'posts', 'create_time', 'user']

    @staticmethod
    def save_comments(post_id, content):
        with db.auto_commit():
            comments = Comments()
            comments.user_id = g.user.uid
            comments.post_id = post_id
            comments.content = content
            db.session.add(comments)

    @staticmethod
    def posts_comments(post_id):
        list = Comments.query.filter_by(post_id=post_id).all()
        return list

    @staticmethod
    def my_comments():
        list = Comments.query.filter_by(user_id=g.user.uid).all()
        return list

    @staticmethod
    def received_comments():
        user_id = g.user.uid
        posts_list = Posts.user_posts(user_id)
        posts_ids = [post.id for post in posts_list]
        list = Comments.query.filter(Comments.post_id.in_(posts_ids), Comments.user_id != user_id).all()
        return list
