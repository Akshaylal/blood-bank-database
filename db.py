from sqlalchemy import Column, Integer, String, Numeric, Float, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///bloodbank.db', echo = False)
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
    donate = relationship('Blood')


class Blood(Base):
    __tablename__ = 'Blood'
    
    code = Column(Integer, primary_key = True)
    amount = Column(Integer)
    blood_type = Column(String)
    did = Column(Integer, ForeignKey('Donor.did'))

class User(Base):
    __tablename__ = 'UserLogin'
    
    uid = Column(Integer, primary_key = True)
    user = Column(String)
    password = Column(String)


Base.metadata.create_all(engine)


Session = sessionmaker(bind = engine)
session = Session()
