# -*- coding: utf-8 -*-
# @Time    : 2018-12-17 15:06
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : ginger.py
# @Software: PyCharm
from app.app import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
