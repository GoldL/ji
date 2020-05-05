# -*- coding: utf-8 -*-
# @Time    : 2020/5/5 下午10:22
# @Author  : iGolden
# @Software: PyCharm
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.reports import Reports
from app.validators.forms import ReportsForm

api = Redprint('reports')


@api.route('', methods=['POST'])
@auth.login_required
def save_reports():
    form = ReportsForm().validate_for_api()
    Reports.save_reports(form.content.data, form.type.data, form.object.data, form.images.data)
    return Success(msg='成功举报！')
