from typing import Collection
from model import Employee
import motor.motor_asyncio #MongoDB driver

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.Employees
collection = database.employees

async def get_employees_by_key_value(key, value):
    employees = []
    cursor = collection.find({key:value})
    async for document in cursor:
        employees.append(Employee(**document))
    return employees


async def get_all_employees():
    employees = []
    cursor = collection.find({})
    async for document in cursor:
        employees.append(Employee(**document))
    return employees

async def create_employee(employee):
    await collection.insert_one(employee)
    return employee

async def update_employee_phone_number(id, phone_number):
    await collection.update_one({'id':id}, 
                                {'$set': {'phone_number':phone_number}})
    document = await collection.find_one({'phone_number':phone_number})
    return document

async def update_employee_address(id, new_address):
    await collection.update_one({'id':id}, 
                                {'$set': {'address':new_address}})
    document = await collection.find_one({'address':new_address})
    return document

async def remove_employee_by_name(name):
    result = await collection.delete_one({'name':name})
    if result.deleted_count == 1:
        return True
    else:
        return False

async def remove_employee_by_id(id):
    result = await collection.delete_one({'id':id})
    if result.deleted_count == 1:
        return True
    else:
        return False