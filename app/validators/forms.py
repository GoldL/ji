# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午11:41
# @Author  : iGolden
# @Software: PyCharm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ParameterException
from app.models.user import User
from app.validators.base import BaseForm as Form


class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='请输入合法邮箱地址')])
    secret = StringField(validators={DataRequired(), Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')})
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ParameterException(msg='该邮箱已被注册')


class PostsForm(Form):
    title = StringField(validators=[DataRequired(), length(min=2, max=32)])
    content = StringField(validators=[DataRequired()])
    images = StringField(validators=[DataRequired()])
    location = StringField(validators=[DataRequired()])


class ReportsForm(Form):
    content = StringField(validators=[DataRequired(), length(min=2, max=255)])
    type = StringField(validators=[DataRequired()])
    object = StringField(validators=[DataRequired()])
    images = StringField()


class PostIdForm(Form):
    post_id = StringField(validators=[DataRequired()])


class UserIdForm(Form):
    user_id = StringField(validators=[DataRequired()])
