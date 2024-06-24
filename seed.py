from random import choice
from random import randint

from faker import Faker
from sqlalchemy import select

from db_config import Session
from models import Group
from models import Score
from models import Student
from models import Subject
from models import Teacher

session = Session

fake = Faker()


def seed_teacher():
    for _ in range(3):
        teacher = Teacher(name=fake.name())
        session.add(teacher)



def seed_group():
    group_name = [f"Group_{i}" for i in range(3)]
    for name in group_name:
        group = Group(name=name)
        session.add(group)



def seed_subject():
    subjects_name = [f"subject_{i}" for i in range(3)]
    teacher_idi = session.scalars(select(Teacher.id)).all()
    for name in subjects_name:
        subject = Subject(name=name, teacher_id=choice(teacher_idi))
        session.add(subject)



def seed_student():
    group_numbers = session.scalars(select(Group.id)).all()
    for _ in range(35):
        student = Student(name=fake.name(), group_id=choice(group_numbers))
        session.add(student)


def seed_score():
    student_id = session.scalars(select(Student.id)).all()
    subject_id = session.scalars(select(Subject.id)).all()
    for _ in range(350):
        score = Score(student_id=choice(student_id), subject_id=choice(subject_id), mark=randint(1, 5), marktime=fake.date())
        session.add(score)


def seed_all():
    seed_teacher()
    seed_group()
    seed_subject()
    seed_student()
    seed_score()
    session.commit()

if __name__ == "__main__":
    seed_all()