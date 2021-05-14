from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.log import echo_property
from sqlalchemy.orm import session, sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Log(Base):
	__tablename__ = 'log'
	id = Column(Integer,nullable=False, primary_key=True,  unique=True)
	serial_num = Column(Text,nullable=False, unique=True)
	timestamp = Column(Integer,nullable=False)
	
	def __init__(self,serial_num, timestamp):
		self.serial_num = serial_num
		self.timestamp = timestamp

class User(Base):
	__tablename__ = 'user'
	id = Column(Integer,nullable=False, primary_key=True, unique=True)
	name = Column(Text,nullable=False)
	serial_num = Column(Text,nullable=False, unique=True)
	curr_count = Column(Integer,nullable=False)

	def __init__(self,name, serial_num):
		self.name = name
		self.serial_num = serial_num

class Pdata(Base):
	__tablename__ = 'pdata'
	id = Column(Integer,nullable=False, primary_key=True, unique=True)
	s_name = Column(Text,nullable=False,unique=True)
	s_val = Column(Text,nullable=False)

	def __init__(self,s_name, s_val):
		self.s_name = s_name
		self.s_val = s_val

def getPdataVal(id):
	return session.query(Pdata).get(id).s_val

def getCurrentCountOfRfid(rfid):
	return session.query(User).filter_by(serial_num=rfid)

def logVending(rfid):
	now=datetime.now()
	timestampz=int(datetime.timestamp(now))
	logx=Log(serial_num=rfid,timestamp=timestampz)
	session.add(logx)
	session.commit()
	print('[INF] Data entered successfully for RFID : ',rfid,'\n')