from turtle import colormode
from fastapi import FastAPI
import uvicorn
from routes.routes import routes
from fastapi.middleware.cors import CORSMiddleware

description = """
## Description

Python API to Create, Read, Update and Delete (CRUD) registries into a given database.

## Options

|**Method**|**Route**|**Description**|
|----------|---------|---------------|
|**GET**|/users|Show a json object with all stored users from database|
|**GET**|/users/{id}|Get user by "id".|
|**POST**|/users|Send a json objetc to add a new registry to database ("id" is optional)|
|**PUT**|/users/{id}|Update the values of a user stored in database|
|**DELETE**|/users/{id}|Search a user by "id" and deletes it from database|
|**DELETE**|/delete_table|Drop the current table from the database|

[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/fegamon)
"""

app = FastAPI(
    title="Fast API - SQL CRUD",
    description=description,
    version='0.1'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(routes)
