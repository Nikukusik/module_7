from db_config import Session
from models import Student, Teacher, Score, Subject, Group
from random import randint
from faker import Faker

if __name__ == "__main__":
    fake = Faker()
    for _ in range(40):
        student = Student(name=fake.name(), group_id=randint(1,3))
        Session.add(student)

    for i in range(3):
        group = Group(name=f"Group_{i}")
        Session.add(group)

    for _ in range(4):
        teacher = Teacher(name=fake.name())
        Session.add(teacher)

    for i in range(7):
        subject = Subject(name=f"subject_{i}", teacher_id=randint(1,4))
        Session.add(subject)

    for _ in range(200):
        score = Score(mark=randint(1,5), subject_id=randint(1,7), student_id=randint(1,40), marktime=f"2024.06.{randint(1,29)}")
        Session.add(score)
    Session.commit()
