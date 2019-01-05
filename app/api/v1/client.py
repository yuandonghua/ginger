# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 2:22 PM
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : client.py
# @Software: PyCharm
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validators.forms import ClientForm, UserEmailForm

api = Redprint('client')


@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_user_by_email(form.nickname.data,
                           form.account.data,
                           form.password.data)
