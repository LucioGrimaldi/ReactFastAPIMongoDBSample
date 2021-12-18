from typing import Collection
from model import Employee
import motor.motor_asyncio #MongoDB driver

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb//localhost:27017')
database = client.Employees
collection = database.employees

async def fetch_one_employee_by_id(id):
    document = await collection.find_one({'id':id})
    return document


async def fetch_all_employees():
    employees = []
    cursor = collection.find({})
    async for document in cursor:
        employees.append(Employee(**document))
    return employees

async def create_employee(employee):
    document = employee
    result = await collection.insert_one(document)
    return document

async def update_employee(id, name, surname, phone_number, address):
    await collection.update_one({'id':id}, 
                                {'$set': {'name':name, 
                                          'surname':surname,
                                          'phone_number':phone_number,
                                          'address':address}})

    document = await collection.find_one({"id":id})
    return document

async def remove_employee(id):
    await collection.delete_one({"id":id})
    return True