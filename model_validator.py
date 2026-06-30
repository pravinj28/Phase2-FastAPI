from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Patient2(BaseModel):
    name: str
    email: EmailStr 
    linkedin_url: AnyUrl
    age: int 
    weight : float 
    married : bool
    allergies: Dict[str, str]
    contact_details: Dict[str,str]

    @model_validator(mode="after")
    def validate_emergency_contact(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients older than 60 miust have emergenct contacts")
        return model

   
def insert_patient_data(patient: Patient2):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted into DB")

patient_info = {"name": "Pravin","email": "abc@hdfc.com", "linkedin_url":"http://linkedin.com/1322", "age": 65, "weight": 75.2, "married": True,"allergies": {"Dust": "Yes"},  "contact_details":{"email": "abc@gmail.com", "phone": "15666545"}}

patient2 = Patient2(**patient_info) #Validation -> type coersion

insert_patient_data(patient2)
