#This is the main script for auto navigating

import sqlalchemy
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float

#We can also make databased saved in flash, but it is
#not as fast as saved in memory
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

#Create a database session
Session = sessionmaker(bind=engine)
session = Session()

#Create a location database class
#Add flags for operations
#flag=1: hover
#flag=2: move forward
#flag=3: move backword
#flag=4: move right
#flag=5: move left
#flag=6: increase height
#flag=7: decrease height
#flag=8: return to charging dock

class Location(Base):
	__tablename__ = 'locs'
	time = Column(Float, primary_key=True)
	front = Column(Float)
	back = Column(Float)
	right = Column(Float)
	left = Column(Float)
	top = Column(Float)
	bottom = Column(Float)
	flag = Column(Integer)
	def __repr__(self):
		return "<User(time='%d', front='%d', back='%d', left='%d', right='%d', top='%d', bottom='%d', flag='%d')>" % (self.time, self.front, self.back, self.left, self.right, self.top, self.bottom, self.flag)

Base.metadata.create_all(engine)

#This is needed to give relative timestamps
ts_start = time.time()

#Main loop
while True:

	time.sleep(5)	
	ts = time.time()
	ts_cur = ts - ts_start

	#To do: add function to read sensor data
	loc = Location(time=ts_cur, front='2', back='3', left='4', right='5', top='6', bottom='57', flag='1')
	session.add(loc)
	session.commit()

	#To do: read database and check operation
	for instance in session.query(Location).order_by(Location.bottom):
		print instance.time, instance.front, instance.flag


session.close_all()
