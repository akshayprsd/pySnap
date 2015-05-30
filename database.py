import sqlalchemy
from sqlalchemy import Column,String,Integer,create_engine
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
class articlecontent(Base):
	__tablename__='Article'
	title=Column(String,nullable=False)
	author=Column(String,nullable=False)
	description=Column(date,nullable=False)
	content=Column(String,nullable=False)
	date=Column(date,nullable=False)
	time=Column(time, nullable=False)
	difficulty=Column(String,nullable=False
	id_num=Column(Integer,nullable=False,primary_key=True)

class articletag(Base):
	__tablename__='Tagid'
	tag_title=Column(String,nullable=False)
	tag_id=Column(Integer,nullable=False,primary_key=True)

class tag(Base):
	__tablename__='Tag'
	tag_id=Column(Integer,nullable=False,primary_key=True)
	id_num=Column(Integer,nullable=False,primary_key=True)

class recent(Base):
	__tablename__='Recent'
	title=Column(String,nullable=False)
	id_num=Column(Integer,nullable=False,primary_key=True)
	url=Column(String,nullable=False)

class unmissable(Base):
	__tablename__='Unmissable'
	title=Column(String,nullable=False)
	id_num=Column(Integer,nullable=False,primary_key=True)
	url=Column(String,nullable=False)

class trending(Base):
	__tablename__='Unmissable'
	title=Column(String,nullable=False)
	id_num=Column(Integer,nullable=False,primary_key=True)
	url=Column(String,nullable=False)

engine=create_engine('sqlite:///test1.db')
Base.metadata.create_all(engine)

