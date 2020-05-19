# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 下午10:22
# @Author  : iGolden
# @Software: PyCharm
import json

from flask import jsonify

from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.posts import Posts
from app.models.reports import Reports
from app.models.user import User
from app.validators.forms import ReportsForm

api = Redprint('reports')


@api.route('', methods=['POST'])
@auth.login_required
def save_reports():
    form = ReportsForm().validate_for_api()
    Reports.save_reports(form.content.data, form.type.data, form.object.data, form.images.data)
    return Success(msg='成功举报！')


@api.route('/list', methods=['GET'])
@auth.login_required
def reports_list():
    list = Reports.list()
    list = jsonify(list)
    return list
    print(list)
    list = [get_object(item) for item in list]
    return list


def get_object(item):
    if item.type == 1:
        object = Posts.query.filter_original(id=item.object).first()
        item.object = jsonify(object)
    else:
        item.object = User.query.filter_original(id=item.object).first()
        item.object = jsonify(object)
    return item
