from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

Base = declarative_base()
user_name = 'your user_name'
password = str('your password')

engine = create_engine('mysql+pymysql://' + user_name + ':' + password + '@localhost')
engine.execute("CREATE DATABASE IF NOT EXISTS studentdatabase")  # create db
engine.execute("USE studentdatabase")
engine.connect()
Session = sessionmaker()
Session.configure(bind=engine)


class Student(Base):
    __tablename__ = 'student'
    roll_number = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    age = Column((Integer))
    gender = Column(String(20))


Base.metadata.create_all(engine)
session = Session()
