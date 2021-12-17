from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
    return 1

@app.get("/api/get_employee_by_id")
async def get_employee_by_id(id):
    return 1

@app.post("/api/add_employee")
async def add_employee(employee):
    return 1

@app.put("/api/put_employee{id}")
async def put_employee(id, employee):
    return 1

@app.delete("/api/delete_employee")
async def delete_employee(id):
    return 1