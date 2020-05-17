# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 上午1:09
# @Author  : iGolden
# @Software: PyCharm
from flask import request, current_app

from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.libs.upload import QiniuUpload

api = Redprint('upload')


@api.route('', methods=['POST'])
@auth.login_required
def upload():
    file = request.files.get('file').read()
    filename = QiniuUpload.upload(file)
    img_url = current_app.config['QINIU_URL'] + filename
    return Success(msg=img_url)


