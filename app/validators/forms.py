# -*- coding: utf-8 -*-
# @Time    : 2019-01-01 15:25
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : forms.py
# @Software: PyCharm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError
from app.models.user import User

from app.validators.base import BaseForm as Form


class ClientForm(Form):
    # 账号
    account = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=32, message='长度不符合要求')])
    # 密码
    password = StringField(validators=[DataRequired(message='不允许为空'), length(min=6, max=32, message='长度不符合要求')])
    # 客户端类型
    type = IntegerField(validators=[DataRequired(message='不允许为空')])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
            self.type.data = client
        except ValueError as e:
            raise e


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='邮箱无效')])
    password = StringField(validators=[DataRequired(), Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])

    def validate_account(self, value):
        '''
        检查邮箱是否存在
        :param value:
        :return:
        '''
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()
