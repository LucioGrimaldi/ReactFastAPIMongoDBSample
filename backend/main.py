from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic.types import Json
from model import Employee
from db import(
    update_employee_phone_number,
    update_employee_address,
    get_all_employees,
    get_employees,
    create_employee,
    remove_employee_by_name,
    remove_employee_by_id,
)
app = FastAPI()

#origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def read_root():
    return {"Test":"Test"}

@app.get("/api/get_employees_list")
async def get_list():
    response = await get_all_employees()
    return response

@app.get("/api/get_employees/")
async def get_employee(key, value):
    response = await get_employees(key, value)
    return response

@app.post("/api/add_employee/", response_model=Employee)
async def add_employee(employee:Employee):
    response = await create_employee(employee.dict())
    #print(response)
    if response:
        return response
    raise HTTPException(400, "Something went wrong, bad request")

@app.put("/api/put_employee/id={id}/address={new_address}/", response_model=Employee)
async def put_employee(id:str, new_address:str):
    response = await update_employee_address(id, new_address)
    if response:
        return response
    raise HTTPException(404, f"Employee with id={id} not found")

@app.put("/api/put_employee/id={id}/phone_number={phone_number}/", response_model=Employee)
async def put_employee(id:str, phone_number:str):
    response = await update_employee_phone_number(id, phone_number)
    if response:
        return response
    raise HTTPException(404, f"Employee with phone_number = {phone_number} not found")

@app.delete("/api/delete_employee/name={name}")
async def delete_employee_by_name(name):
    response = await remove_employee_by_name(name)
    if response == True:
        return f"Employee with name = {name} correclty deleted."
    raise HTTPException(404, f"Employee with name = {name} not found")

@app.delete("/api/delete_employee/id={id}")
async def delete_employee_by_id(id):
    response = await remove_employee_by_id(id)
    if response == True:
        return f"Employee with id = {id} correclty deleted."
    raise HTTPException(404, f"Employee with id = {id} not found")