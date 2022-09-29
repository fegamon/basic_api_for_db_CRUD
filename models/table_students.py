from enum import unique
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

# table students
students = Table("students", meta,
                 Column('id', Integer, primary_key=True),
                 Column('nombre', String(50)),
                 Column('apellido', String(50)),
                 Column('edad', Integer),
                 Column('cedula', String(10), unique=True),
                 Column('email', String(255)),
                 Column('genero', String(1)))

meta.create_all(engine)
