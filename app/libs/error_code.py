# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 上午1:31
# @Author  : iGolden
# @Software: PyCharm
from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    error_code = -1


class ServerError(APIException):
    code = 500
    msg = '未知错误异常'
    error_code = 999


class ClientTypeError(APIException):
    code = 400
    msg = '客户端类型有误'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = '参数有误'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = '资源未找到'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = '未授权'
    error_code = 1005


class Forbidden(APIException):
    code = 403
    msg = '无权限操作'
    error_code = 1004
