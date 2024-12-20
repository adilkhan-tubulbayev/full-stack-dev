
# Back-End 101 Final Project

## Simple To-Do List Manager web-application based on FastAPI & SwaggerUI

## Installing Dependencies via Poetry


poetry add fastapi uvicorn

## Application Launch

we can use local server for app testing:  
poetry shell  
poetry run uvicorn main:app --reload

## Example of using API

- Open the link to the documentation in your browser: 
  - Swagger UI: [text](http://127.0.0.1:8000/docs)  
	- ReDoc: [text](http://127.0.0.1:8000/redoc)
- Browse the available options
- Test the endpoints directly in the interface by providing different input values (look at the name of the defaults) by clicking "Try it out"  

