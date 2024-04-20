import sqlalchemy

from data.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Account(SqlAlchemyBase, SerializerMixin):
    __tablename__ = "Accounts"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, nullable=False)
    fname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    lname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    names = sqlalchemy.Column(sqlalchemy.String, nullable=True)
