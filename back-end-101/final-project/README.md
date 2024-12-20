
# Back-End 101 Final Project

> A simple web application for managing to-do lists, built with FastAPI and SwaggerUI for API documentation.

## Installing Dependencies via Poetry

```
poetry add fastapi uvicorn
```

## Application Launch

> We can use local server for app testing: 

```
poetry shell  
poetry run uvicorn main:app --reload
```

## Example of using API

1. Open the link to the documentation in your browser: 
   - [Open SwaggerUI](http://127.0.0.1:8000/docs)
   - [Open ReDoc](http://127.0.0.1:8000/redoc)
2. Browse the available options
3. Test the endpoints directly in the interface by providing different input values (look at the name of the defaults) by clicking "Try it out"  