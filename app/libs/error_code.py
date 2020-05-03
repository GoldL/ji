# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 上午1:31
# @Author  : iGolden
# @Software: PyCharm
from app.libs.error import APIException


class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006
