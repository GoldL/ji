# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 上午11:19
# @Author  : iGolden
# @Software: PyCharm
from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建超级管理员
        user = User()
        user.nickname = 'admin'
        user.password = '123456'
        user.email = 'admin@qq.com'
        user.avatar = 'http://qiniu.youbego.top/avatar.jpg'
        user.auth = 2
        db.session.add(user)
