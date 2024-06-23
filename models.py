from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship
from db_config import engine

Base = declarative_base()


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey("groups.id"))


class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)


class Subject(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey("teachers.id"))


class Score(Base):
    __tablename__ = 'scores'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.id"))
    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey("subjects.id"))
    mark: Mapped[int] = mapped_column(Integer, nullable=False)
    marktime: Mapped[str] = mapped_column(String, nullable=False)

