# -*- coding: utf-8 -*-
# @Time    : 2019-01-01 18:38
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : base.py
# @Software: PyCharm
from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        super(BaseForm, self).__init__(data=request.json)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self
