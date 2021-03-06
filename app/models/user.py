# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午11:56
# @Author  : iGolden
# @Software: PyCharm
from sqlalchemy import Column, Integer, String, SmallInteger, orm
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(32), unique=True)
    avatar = Column(String(240), default='http://qiniu.youbego.top/avatar.jpg')
    sex = Column(SmallInteger, default=1)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    @orm.reconstructor
    def __init__(self):
        super(User, self).__init__()
        self.fields = ['id', 'avatar', 'sex', 'email', 'nickname', 'status']

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_original(email=email).first()
        if user.status == 0:
            raise AuthFailed(msg='账号已被禁用，请联系管理员', error_code=1008)
        if not user.check_password(password):
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'scope': scope}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

    @classmethod
    def user_list(cls):
        user_list = User.query.filter_original().all()
        return user_list
