import email
from fastapi import APIRouter
from config.db import connection, engine
from models.table import table
from schemas.table_schema import tableSchema
from sqlalchemy import or_
from starlette.status import HTTP_200_OK

routes = APIRouter()

# show table list
@routes.get('/users', response_model=list[tableSchema], tags=['CRUD'], 
                    description='List all data from table.')
def list_all_data():
    try:
        return connection.execute(table.select()).fetchall()

    except Exception as error:
        return error

# add a new registry
@routes.post('/users', tags=['CRUD'], description='Add a new registry to table')
def add_registry(tableSchema: tableSchema):
    try:
        new_registry = {'id': tableSchema.id,
                    'name': tableSchema.name,
                    'last_name': tableSchema.last_name,
                    'age': tableSchema.age,
                    'phone': tableSchema.phone,
                    'email': tableSchema.email}

        result = connection.execute(table.insert().values(new_registry))
        return HTTP_200_OK

    except Exception as error:
        return error

# get a registry by id
@routes.get('/users/{id}', response_model=tableSchema, tags=['CRUD'], 
                    description='Get a registry by id.')
def get_registry(id: str):
    try:
        result = connection.execute(table.select().where(
            table.c.id == id
        )).first()
        return result
        
    except Exception as error:
        return error

# delete a registry by id
@routes.delete('/users/{id}', tags=['CRUD'], description='Delete a registry by id.')
def delete_registry(id: str):
    try:
        result = connection.execute(table.delete().where(table.c.id == id))
        return HTTP_200_OK

    except Exception as error:
        return error

# update registry't values
@routes.put('/users/{id}', response_model=tableSchema, tags=['CRUD'], 
                    description='Update registry of a specific by id.')
def update_registry(id: str, tableSchema: tableSchema):
    try:
        connection.execute(table.update().values(
            name=tableSchema.name,
            last_name=tableSchema.last_name, 
            age=tableSchema.age,
            phone=tableSchema.phone, 
            email=tableSchema.email
            ).where(table.c.id == id))
        return connection.execute(table.select().where(table.c.id == id)).first()

    except Exception as error:
        return error

# drop current database
@routes.delete('/delete_table', tags=['Table'], description='Drop current database.')
def delete_table():
    try:
        connection.execute(table.drop(engine))
        return HTTP_200_OK
    except Exception as err:
        return err