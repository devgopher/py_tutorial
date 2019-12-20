import sqlalchemy.orm
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Text,   create_engine, UniqueConstraint,  PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSON,  FLOAT,  TIMESTAMP,  INTEGER
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import datetime;
import uuid;

Base = declarative_base()

class track_points(Base):
    __tablename__ = 'track_points'
    __table_args__ = (
        PrimaryKeyConstraint('id', 'moment'),
    )
    id = Column('id',  UUID(),  nullable=False)
    x = Column('x', FLOAT(), nullable=False)
    y = Column('y', FLOAT(), nullable=False)
    moment = Column('moment', TIMESTAMP(), nullable=False)

def add_point(x, y, z) :
    point = track_points()
    point.id = str(uuid.uuid4())
    point.x = x
    point.y = y
    point.moment = datetime.datetime.now()

    engine = sa.create_engine("postgresql+psycopg2://postgres:12345678@52.178.139.170:5432/tutorial")

    session = sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker(engine))
    session.add(point)
    session.flush()

    print("UUID: " + str(point.id))

def get_last_points(count):
    engine = sa.create_engine("postgresql+psycopg2://postgres:12345678@52.178.139.170:5432/tutorial")
   
    session = sqlalchemy.orm.scoped_session(sqlalchemy.orm.sessionmaker(engine))
    results = session.query(track_points).order_by(track_points.moment.desc()).limit(count)
    
    for res in results :
        print("point# " + str(res.id) + ": "+ str(res.moment)+ "  (x;y): (" + str(res.x)  + " , "+ str(res.y) + ")")