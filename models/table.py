from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

# table students
table = Table("user", meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('last_name', String(50)),
    Column('age', Integer),
    Column('phone', Integer),
    Column('email', String(50)))

meta.create_all(engine)
