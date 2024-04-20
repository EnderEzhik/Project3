import sqlalchemy

from sqlalchemy import orm
from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class BlackList(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "BlackList"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Accounts.user_id"), unique=True)
    
    accounts = orm.relationship("Account")
