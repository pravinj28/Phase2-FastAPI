#This is to export in json and dictionary


from pydantic import BaseModel


class Address(BaseModel):
    city: str
    state: str
    pin: str                        #we create a model where address is defined and then we can use that in our basemodel
class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address


address_dict = {"city": "jalgaon", "state": "Maharashtra", "pin": "425001"}

address1 = Address(**address_dict)

patient_dict = {"name": "Pravin", "gender": "male", "age": 22, "address": address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(include=["name"])  #it will give you only name field also you have exclude option 

print(temp)
print(type(temp))

temp2 = patient1.model_dump_json()
print(temp2)
print(type(temp2))


