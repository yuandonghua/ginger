# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 16:51
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : user.py
# @Software: PyCharm
from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('/user/get')
def get_user():
    pass
