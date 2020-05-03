# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 下午10:04
# @Author  : iGolden
# @Software: PyCharm
from app.app import create_app

app = create_app()

if __name__ == '__main__':
    
    app.run(debug=True)
