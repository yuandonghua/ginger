# -*- coding: utf-8 -*-
# @Time    : 2019-01-01 15:51
# @Author  : 袁东华
# @Email   : 1348474384@qq.com
# @File    : user.py
# @Software: PyCharm
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    # 有权限，1普通用户，2管理员
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(200))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    @staticmethod
    def register_user_by_email(nickname, account, password):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = password
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid': user.id, 'scope': scope}

    def check_password(self, password):
        if not self._password:
            return False
        return check_password_hash(self._password, password)

    def keys(self):
        return ['id', 'email', 'nickname', 'auth']
