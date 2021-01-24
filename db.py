from sqlalchemy import Column, Integer, String, Numeric, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///bloodbank.db', echo = True)
Base = declarative_base()


class Donor(Base):
    __tablename__ = 'Donor'
    
    did = Column(Integer, primary_key = True)
    name = Column(String)
    sex = Column(String)
    age = Column(Integer)
    blood_type = Column(String)
    address = Column(String)
    phone = Column(Numeric(precision = 10, asdecimal = False, decimal_return_scale = None))


class Blood(Base):
    __tablename__ = 'Blood'
    
    code = Column(Integer, primary_key = True)
    amount = Column(Integer)
    blood_type = Column(String)
    did = Column(Integer)


Base.metadata.create_all(engine)


Session = sessionmaker(bind = engine)
session = Session()
