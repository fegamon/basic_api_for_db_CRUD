from sqlalchemy import create_engine, MetaData

# connect to data base
engine = create_engine('mysql+pymysql://root:@localhost/db_name')
meta = MetaData()
connection = engine.connect()