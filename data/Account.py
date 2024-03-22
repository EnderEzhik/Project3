import sqlalchemy

from .db_session import SqlAlchemyBase


class Account(SqlAlchemyBase):
    __tablename__ = "Accounts"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, nullable=False)
    fname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    lname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    names = sqlalchemy.Column(sqlalchemy.String, nullable=True)
