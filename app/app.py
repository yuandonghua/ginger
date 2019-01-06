# -*- coding: utf-8 -*-
# @Time    : 2018-12-17 14:42
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : app.py
# @Software: PyCharm
from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder

