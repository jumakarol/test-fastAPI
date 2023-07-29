from database import Base
from sqlalchemy import Column,Integer, String, Boolean



class Pages(Base):
	__tablename__ = 'pages'
	id = Column(Integer, primary_key = True, index = True)
	title = Column(String)
	body = Column(String)
	published = Column(Boolean)


