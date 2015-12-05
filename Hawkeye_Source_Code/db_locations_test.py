import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Location(Base):
	__tablename__ = 'locs'
	time = Column(Integer, primary_key=True)
	front = Column(Integer)
	back = Column(Integer)
	right = Column(Integer)
	left = Column(Integer)
	top = Column(Integer)
	bottom = Column(Integer)
	def __repr__(self):
		return "<User(time='%d', front='%d', back='%d', left='%d', right='%d', top='%d', bottom='%d')>" % (self.time, self.front, self.back, self.left, self.right, self.top, self.bottom)

Base.metadata.create_all(engine)

loc1 = Location(time='1', front='2', back='3', left='4', right='5', top='6', bottom='57')
loc2 = Location(time='21', front='22', back='23', left='24', right='25', top='26', bottom='47')
loc3 = Location(time='31', front='32', back='33', left='34', right='35', top='36', bottom='37')
loc4 = Location(time='41', front='42', back='43', left='44', right='45', top='46', bottom='27')
loc5 = Location(time='51', front='52', back='53', left='54', right='55', top='56', bottom='7')

session.add(loc1)
session.add(loc2)
session.add(loc3)
session.add(loc4)
session.add(loc5)

session.commit()

for instance in session.query(Location).order_by(Location.bottom):
	print instance.time, instance.front
	

session.close_all()
