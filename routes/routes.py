import email
from fastapi import APIRouter
from config.db import connection, engine
from models.table_students import students
from schemas.student_schema import studentSchema
from sqlalchemy import or_
from starlette.status import HTTP_200_OK

api_students = APIRouter()

# show students list
@api_students.get('/students', response_model=list[studentSchema], tags=['Students'], 
                    description='List all students from database.')
def list_all_students():
    try:
        return connection.execute(students.select()).fetchall()

    except Exception as error:
        return error

# add a new student
@api_students.post('/students', tags=['Students'], description='Add a new student to database')
def add_student(studentSchema: studentSchema):
    try:
        new_student = {'id': studentSchema.id,
                    'nombre': studentSchema.nombre,
                    'apellido': studentSchema.apellido,
                    'edad': studentSchema.edad,
                    'cedula': studentSchema.cedula,
                    'email': studentSchema.email,
                    'genero': studentSchema.genero}

        result = connection.execute(students.insert().values(new_student))
        return HTTP_200_OK

    except Exception as error:
        return error

# get a student by 'cedula' or 'apellido'
@api_students.get('/students/{value}', response_model=studentSchema, tags=['Students'], 
                    description='Get a student from "cedula" or "apellido" key.')
def get_students(value: str):
    try:
        result = connection.execute(students.select().where(or_(
            students.c.cedula == value, students.c.apellido == value
        ))).first()
        return result
        
    except Exception as error:
        return error

# delete a student from a given id
@api_students.delete('/students/{id}', tags=['Students'], description='Delete a student from database.')
def delete_student(id: str):
    try:
        result = connection.execute(students.delete().where(students.c.id == id))
        return HTTP_200_OK

    except Exception as error:
        return error

# update studen't values
@api_students.put('/students/{id}', response_model=studentSchema, tags=['Students'], 
                    description='Update valures of a specific student.')
def update_student(id: str, studentSchema: studentSchema):
    try:
        connection.execute(students.update().values(nombre=studentSchema.nombre,
                        apellido=studentSchema.apellido, edad=studentSchema.edad,
                        cedula=studentSchema.cedula, email=studentSchema.email,
                        genero=studentSchema.genero).where(students.c.id == id))
        return connection.execute(students.select().where(students.c.id == id)).first()

    except Exception as error:
        return error

# drop current database
@api_students.delete('/delete_table', tags=['Students'], description='Drop current database.')
def delete_table():
    try:
        connection.execute(students.drop(engine))
        return HTTP_200_OK
    except Exception as err:
        return err