# -*- coding: utf-8 -*-
# @Time    : 2018-12-26 16:49
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : book.py
# @Software: PyCharm
from app.libs.redprint import Redprint

api = Redprint('book');


@api.route('', methods=['GET'])
def get_book():
    return 'get book'


@api.route('', methods=['POST'])
def create_book():
    return 'create book'
