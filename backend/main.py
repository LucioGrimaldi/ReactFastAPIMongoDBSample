from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.model import Employee, Employees
from db import(
    fetch_one_employee_by_id,
    fetch_all_employees,
    create_employee,
    update_employee,
    remove_employee
)
app = FastAPI()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def read_root():
    return {"Test":"Test"}

@app.get("/api/get_employees_list")
async def get_list():
    response = await fetch_all_employees()
    return response

@app.get("/api/get_employee_by_id", response_model=Employee)
async def get_employee_by_id(id):
    response = await fetch_one_employee_by_id(id)
    if response:
        return response
    raise HTTPException(404, f"Employee with id={id} not found")

@app.post("/api/add_employee", response_model=Employee)
async def add_employee(employee):
    return 1

@app.put("/api/put_employee{id}")
async def put_employee(id, employee):
    return 1

@app.delete("/api/delete_employee")
async def delete_employee(id):
    return 1