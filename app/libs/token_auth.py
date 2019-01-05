# -*- coding: utf-8 -*-
# @Time    : 2019-01-04 15:17
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : token_auth.py
# @Software: PyCharm
from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed

auth = HTTPBasicAuth()

User = namedtuple('User', ['uid', 'type', 'scope'])


@auth.verify_password
def verify_password(token, password):
    user = verify_auth_token(token)
    if not user:
        return False
    else:
        g.user = user
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token无效', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token过期', error_code=1003)
    uid = data['uid']
    type = data['type']

    return User(uid, type, None)
