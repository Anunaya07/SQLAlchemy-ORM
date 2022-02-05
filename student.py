from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///alchemy.db', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__='student'
    
    id=Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade= Column(String(50))

#Base.metadata.create_all(engine)


#inserting table

# =============================================================================
# student1 = Student(name="Jerin", age=27, grade="Fifth")
# student2 = Student(name="Ann", age=24, grade="Fourth")
# student3 = Student(name="Jefin", age=21, grade="Third")
# 
# 
# # session.add(student1);
# session.add_all([student2, student3])
# 
# session.commit()
# =============================================================================
    
# =============================================================================
# # reading data from the table
# 
# # get all data
# students = session.query(Student)
# for student in students:
#     print(student.name, student.age, student.grade)
#     
# print('\n'*5)
#     
# #get data in order
# students = session.query(Student).order_by(Student.name)
# 
# for student in students:
#     print(student.name)
#     
# print('\n'*5)
# 
# 
# #get data by filtering
# 
# student = session.query(Student).filter(Student.name=="Jerin").first()
# print(student.name, student.age)
# print("\n"*5)
# 
# # number of values
# student_count = session.query(Student).filter(or_(Student.name=="Jerin", Student.name=="Ann")).count()
# print(student_count)
# =============================================================================

# =============================================================================
# #Update data
# student = session.query(Student).filter(Student.name=="Jerin").first()
# student.name="Kevin"
# session.commit()
# =============================================================================


# =============================================================================
# #delete the record
# student = session.query(Student).filter(Student.name=="Kevin").first()
# session.delete(student)
# session.commit()
# =============================================================================
