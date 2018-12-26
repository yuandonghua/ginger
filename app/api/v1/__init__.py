# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 16:52
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : __init__.py
# @Software: PyCharm
from flask import Blueprint
from app.api.v1 import book, user


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    book.api.register(bp_v1)
    user.api.register(bp_v1)
    return bp_v1
