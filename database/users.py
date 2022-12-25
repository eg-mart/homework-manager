import enum
import json
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Table
from sqlalchemy.orm import relationship
from database.db_session import SqlAlchemyBase, create_session
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import check_password_hash, generate_password_hash


class UserType(enum.Enum):
    user = 0
    student = 1
    teacher = 2


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    hashed_password = Column(String)

    user_type = Column(Enum(UserType))

    __mapper_args__ = {
        "polymorphic_identity": UserType.user,
        "polymorphic_on": user_type,
        "with_polymorphic": "*",
    }

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


student_to_homework = Table(
    "student_to_homework",
    SqlAlchemyBase.metadata,
    Column("student_id", ForeignKey("student.id"), primary_key=True),
    Column("homework_id", ForeignKey("homework.id"), primary_key=True)
)


class Student(User):
    __tablename__ = 'students'
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    grade = Column(String)
    priorities = Column(String)
    schedule_json = Column(String)
    homework = relationship("Homework", secondary=student_to_homework)


    __mapper_args__ = {
        "polymorphic_identity": UserType.student,
    }

    @property
    def schedule(self):
        result = dict()
        data = json.load(self.schedule_json)

        for day in data:
            result[day] = []
            for hw in self.homework:
                if hw.id in data[day]:
                    result[day].append(hw)

        return result

    @schedule.setter
    def schedule(self, data):
        result = dict()
        for day in data:
            result[day] = [hw.id for hw in data[day]]
        
        self.schedule_json = json.dump(result)


class Teacher(User):
    __tablename__ = 'teachers'
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    subject = Column(String)

    __mapper_args__ = {
        "polymorphic_identity": UserType.teacher,
    }

