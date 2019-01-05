# -*- coding: utf-8 -*-
# @Time    : 2018-12-17 15:06
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : ginger.py
# @Software: PyCharm
from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    '''
    全局异常处理
    :param e:
    :return:
    '''
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(msg, code, error_code)
    else:
        # 记录日志
        if app.config['DEBUG']:
            return e
        else:
            return ServerError()


if __name__ == '__main__':
    app.run(debug=True)
