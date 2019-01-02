# -*- coding: utf-8 -*-
# @Time    : 2019-01-01 18:00
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : error.py
# @Software: PyCharm

from flask import request, json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = '服务器内部错误'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if msg:
            self.msg = msg
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(msg=self.msg,
                    error_code=self.error_code, request=request.method + ' ' + self.get_url_no_param())
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        match_path = full_path.split('?')
        return match_path[0]
