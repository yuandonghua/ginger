# -*- coding: utf-8 -*-
# @Time    : 2019-01-06 18:57
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : scope.py
# @Software: PyCharm
class Scope():
    allow_api = set()
    allow_module = set()
    forbidden = set()

    def __add__(self, other):
        self.allow_api = self.allow_api | other.allow_api
        self.allow_module = self.allow_module | other.allow_module
        self.forbidden = self.forbidden | other.forbidden
        return self


class AdminScope(Scope):
    # allow_api = {'v1.user+super_get_user'}
    allow_module = {'v1.user'}

    # def __init__(self):
    #     self + UserScope()


class UserScope(Scope):
    # allow_api = {'v1.user+get_user'}
    forbidden = {'v1.user+super_get_user'}

    def __init__(self):
        self + AdminScope()


def is_in_scope(scope, endpoint):
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]
    if endpoint in scope.forbidden:
        return False
    elif endpoint in scope.allow_api:
        return True
    elif red_name in scope.allow_module:
        return True
    else:
        return False
