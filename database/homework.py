import sqlalchemy
from database.db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Homework(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'homework'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    data = sqlalchemy.Column(sqlalchemy.String)
    subject = sqlalchemy.Column(sqlalchemy.String)
    grade = sqlalchemy.Column(sqlalchemy.String)
    deadline = sqlalchemy.Column(sqlalchemy.DateTime)

