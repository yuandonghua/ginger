# -*- coding: utf-8 -*-
# @Time    : 2019-01-05 16:00
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : fake.py
# @Software: PyCharm
from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():
    with db.auto_commit():
        # 创建一个管理员
        user = User()
        user.nickname = 'Super'
        user.password = '123qwe'
        user.email = '88888888@qq.com'
        user.auth = 2
        db.session.add(user)


