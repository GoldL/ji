# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 下午10:14
# @Author  : iGolden
# @Software: PyCharm
from flask import g
from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey, orm
from sqlalchemy.orm import relationship

from app.models.base import Base, db


class Reports(Base):
    id = Column(Integer, primary_key=True)
    content = Column(String(255))
    images = Column(String(255))
    type = Column(SmallInteger, default=1)
    object = Column(Integer)
    user = relationship('User')
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'content', 'images', 'type', 'object', 'user', 'create_time', 'user_id', 'status']

    @staticmethod
    def save_reports(content, type, object, images):
        with db.auto_commit():
            reports = Reports()
            reports.user_id = g.user.uid
            reports.content = content
            reports.type = type
            reports.object = object
            reports.images = images
            db.session.add(reports)

    @classmethod
    def list(cls):
        list = Reports.query.filter_by().all()
        return list
