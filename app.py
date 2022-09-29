from turtle import colormode
from fastapi import FastAPI
from routes.routes import api_students

description = """
# Student API to MySql CRUD. 🚀

## Usage

List, add, update and delete users from database.

## Options

|**Method**|**Route**|**Description**|
|----------|---------|---------------|
|**GET**|/students|Show a json object with all stored students from database|
|**POST**|/students|Send a json objetc to add a new student to database ("id" is optional)|
|**GET**|/students/{value}|Search for a student in database. Into "value" insert a "cedula" or "apellido" key|
|**PUT**|/students/{id}|Update the values of a student stored in database|
|**DELETE**|/students/{id}|Search a student by "id" and deletes it from database|
|**DELETE**|/delete_table|Drop the current table from the database|

**Developed by Freddy Granda & Ariel Torres.**

[GitHub Repository](https://github.com/fegamon/student_db_api.git)
"""

app = FastAPI(
    title="Student's API",
    description=description,
    version='0.0.1',
    openapi_tags=[{
        'name': 'Students',
        'description': "API for student's CRUD in MySql"
    }]
)
app.include_router(api_students)
