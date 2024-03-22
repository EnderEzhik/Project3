import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class BlackList(SqlAlchemyBase):
    __tablename__ = "BlackList"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Accounts.user_id"), unique=True)
    accounts = orm.relationship("Account")
