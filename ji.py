# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午10:04
# @Author  : iGolden
# @Software: PyCharm
from app import create_app
from app.libs.error import APIException, HTTPException
from app.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        if not app.config['DEBUG']:
            return ServerError()
        else:
            raise e


if __name__ == '__main__':
    app.run(debug=True, port=3004)
