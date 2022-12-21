import sqlalchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from database.db_session import SqlAlchemyBase
from werkzeug.security import check_password_hash, generate_password_hash


class Teacher(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'teachers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    subject = sqlalchemy.Column(sqlalchemy.String)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
