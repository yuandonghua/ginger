# -*- coding: utf-8 -*-
# @Time    : 2019-01-04 14:21
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : token.py
# @Software: PyCharm
from flask import current_app
from flask.json import jsonify

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify
    }
    #
    identify = promise[ClientTypeEnum(form.type.data)](form.account.data, form.password.data)
    expiration = current_app.config['TOKEN_EXPIRATION']
    token = generate_auth_token(identify['uid'], form.type.data, None, expiration)
    t = {
        'token': token.decode('ascii')
    }
    return jsonify(t),201


def generate_auth_token(uid, ac_type, scope=None, expiration=7200):
    '''
    生成令牌
    :param uid:
    :param ac_type:
    :param scope:
    :param expiration:
    :return:
    '''
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'uid': uid, 'type': ac_type.value})



