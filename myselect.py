from db_config import Session

from sqlalchemy import func, select, desc, and_

from models import Student, Score, Subject, Teacher, Group

if __name__ == "__main__":

    select_1 = Session.query(Student.name, func.round(func.avg(Score.mark), 2).label('avg_grade')).select_from(Score).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

    #select_2 = Session.execute(select(Student.name, Subject.name, func.round(func.avg(Score.mark), 2).label('avg_grade')).select_from(Score).join(Student).join(Subject).where(Student.id == 1).order_by(desc('avg_grade'))) #TODO

    #select_3 = Session.execute(select(Subject.name, func.avg(Score.mark)).select_from(Score).join(Subject).where(Subject.id == 1)) #TODO

    select_4 = Session.execute(select(func.avg(Score.mark)).select_from(Score)).all()

    select_5 = Session.execute(select(Subject.name).select_from(Subject).where(Subject.teacher_id == 2)).all()

    select_6 = Session.execute(select(Student.name).select_from(Student).where(Student.group_id == 2)).all()

    select_7 = Session.execute(select(Score.mark, Group.name, Subject.name).select_from(Score).join(Student).join(Group).join(Subject).where(and_(Group.id == 1, Subject.id == 1))).all()

    select_8 = Session.execute(select(func.avg(Score.mark)).select_from(Score).join(Subject).join(Teacher).where(Teacher.id == 3)).all()

    select_9 = Session.execute(select(Student.name, Subject.name).select_from(Score).where(Student.id == 1).join(Student).join(Subject)).all()