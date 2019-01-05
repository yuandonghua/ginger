# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 16:51
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : user.py
# @Software: PyCharm
from flask import jsonify

from app.libs.error_code import NotFound
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    r={
        'nickname':user.nickname
    }
    return jsonify(r)
