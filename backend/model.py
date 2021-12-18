#create json schemas from model
from pydantic import BaseModel

class Employees(BaseModel):
    id : int
    name : str
    surname : str
    phone_number : str
    address : str
