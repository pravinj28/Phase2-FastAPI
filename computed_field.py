#field where value is not provided by user

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, computed_field
from typing import List, Dict, Optional, Annotated


class Patient2(BaseModel):
    name: str
    email: EmailStr 
    linkedin_url: AnyUrl
    age: int 
    weight : float    #kg
    height : float #meters
    married : bool
    
    allergies: Dict[str, str]
    contact_details: Dict[str,str]

@computed_field #this is the computed field and we do not require user input for it, it is calculated by code itself
@property
def bmi(self) -> float:
    bmi = round(self.weight/(self.height**2), 2)
    return bmi

   
def insert_patient_data(patient: Patient2):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("BMI", patient.bmi)
    print("Inserted into DB")

patient_info = {"name": "Pravin","email": "abc@hdfc.com", "linkedin_url":"http://linkedin.com/1322", "age": 65, "weight": 75.2,"height": 1.72, "married": True,"allergies": {"Dust": "Yes"},  "contact_details":{"email": "abc@gmail.com", "phone": "15666545"}}

patient2 = Patient2(**patient_info) #Validation -> type coersion

insert_patient_data(patient2)
