# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 16:51
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : user.py
# @Software: PyCharm
from flask import jsonify, g

from app.libs.error_code import NotFound, DeleteSuccess, AuthFailed
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.models.base import db
from app.models.user import User

api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    is_admin = g.user.is_admin
    if not is_admin:
        raise AuthFailed()
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        user.delete()
    return DeleteSuccess()


@api.route('/<int:uid>', methods=['DELETE'])
def super_delete_user(uid):
    pass
