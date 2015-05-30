from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base,articlecontent,articletag,recent,tag,unmissable,trending,engine

Base.metadata.bind=engine
DBSession=sessionmaker(bind=engine)
session=DBSession()

def add_new(new_entry):
	session.add(new_entry)
	session.commit()

def edit_entry(id_num,embed_url,title,thumbnail_url,description):
	entry=session.query(YTLink1).filter_by(id_num=id_num)
	entry.embed_url=embed_url
	entry.title=title
	entry.thumbnail_url=thumbnail_url
	entry.description=description
	entry.id_num=id_num

def delete_entry(id_num):
	entry=session.query(YTLink1).filter_by(id_num=id_num)
	session.delete(entry)
	session.commit()
