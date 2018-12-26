# -*- coding: utf-8 -*-
# @Time    : 2018-12-17 14:42
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : app.py
# @Software: PyCharm
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')
