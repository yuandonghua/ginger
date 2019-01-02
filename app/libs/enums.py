# -*- coding: utf-8 -*-
# @Time    : 2019-01-01 15:21
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : enums.py
# @Software: PyCharm
from enum import Enum


class ClientTypeEnum(Enum):
    # 邮箱登陆
    USER_EMAIL = 100
    # 手机号登陆
    USER_PHONE = 101
    # QQ登陆
    USER_QQ = 200
    # 微信登陆
    USER_WX = 201
