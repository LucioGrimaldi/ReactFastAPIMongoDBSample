#create json schemas from model
from pydantic import BaseModel

class Employee(BaseModel):
    id : str
    name : str
    surname : str
    phone_number : str
    address : str
