# -*- coding: utf-8 -*-
# @Time    : 2019-01-01 17:47
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : error_code.py
# @Software: PyCharm
from werkzeug.exceptions import HTTPException

from app.libs.error import APIException

class ServerError(APIException):
    code = 500
    msg = '服务器内部错误'
    error_code = 500

class Fail(APIException):
    code = 400
    msg = '操作失败'
    error_code = 1001

    def __init__(self, msg=None):
        if msg:
            self.msg = msg
        super(Fail, self).__init__()


class Success(APIException):
    code = 201
    msg = '操作成功'
    error_code = 200


class ClientTypeError(APIException):
    code = 400
    msg = '客户端类型错误'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = '参数错误'
    error_code = 1000
