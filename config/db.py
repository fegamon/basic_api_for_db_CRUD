from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

#get enviroment
load_dotenv()

DB_ENGINE = os.getenv('DB_ENGINE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')

# connect to data base
engine = create_engine('{0}://{1}:{2}@{3}/{4}'.format(DB_ENGINE, DB_USER, DB_PASSWORD, DB_HOST, DB_NAME))

meta = MetaData()   
connection = engine.connect()