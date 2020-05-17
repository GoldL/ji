# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 上午2:06
# @Author  : iGolden
# @Software: PyCharm
from flask import current_app
from qiniu import Auth, put_data


class QiniuUpload:
    @classmethod
    def upload(cls, file):
        q = Auth(current_app.config['QINIU_ACCESS_KEY'], current_app.config['QINIU_SECRET_KEY'])
        token = q.upload_token(current_app.config['QINIU_BUCKET'])
        # 如果需要对上传的图片命名，就把第二个参数改为需要的名字
        # 如果需要对上传的图片命名，就把第二个参数改为需要的名字
        ret1, ret2 = put_data(token, None, data=file)
        print('ret1:', ret1)
        print('ret2:', ret2)

        # 判断是否上传成功
        if ret2.status_code != 200:
            raise Exception('文件上传失败')

        return ret1.get('key')
