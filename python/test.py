# from config import pguser, pw
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
import os


#create your database in pgadmin4 as twitter_data
# db_string = f'postgresql://{pguser}:{pw}@localhost:5432/twitter_data'
# db = os.environ.get('DATABASE_URL')
# engine = create_engine(db)

connection_string ="postgres:Shjais2014@localhost:5432/twitter_db"
engine = create_engine(f'postgresql://{connection_string}')
# engine = create_engine(db_string)
print('Loading Engine...')

Base = declarative_base()


# Defining Schema

class MainJSON (Base):
        __tablename__ = 'twitter_tweets'
        ID = Column("id", Integer, primary_key=True)
        Tweets = Column('Tweets', JSON)

MainJSON.__table__.create(bind = engine, checkfirst = True)


Base.metadata.create_all(engine)
print('Loading Schema...')

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


print('Loading Complete.')