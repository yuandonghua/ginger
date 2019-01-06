# -*- coding: utf-8 -*-
# @Time    : 2019-01-06 18:57
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : scope.py
# @Software: PyCharm
class AdminScope():
    allow_api = ['super_get_user']


class AdminScope():
    allow_api = ['']


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False
