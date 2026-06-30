#TYPE VALIDATION
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    
    name: Annotated[str, Field(max_length = 50, title = "Name of the patient", description= " Give the name of the patient in less than 50 characters", examples= ["Pravin", "Nitish"])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt = 0, lt = 120)
    weight : Annotated[float , Field(gt = 0, strict= True)]
    married : Annotated[bool, Field(default = None, description="Is the patient married or not?")] #setting up the default values
    allergies: Annotated[Optional[List[str]] , Field(default= None, max_length=5)] #this are optional fields
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

    print("Inserted into DB")

patient_info = {"name": "Pravin","email": "abc@gmail.com", "linkedin_url":"http://linkedin.com/1322", "age": 30, "weight": 75.2, "married": True,  "contact_details":{"email": "abc@gmail.com", "phone": "15666545"}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)

class Patient2(BaseModel):
    name: str
    email: EmailStr 
    linkedin_url: AnyUrl
    age: int 
    weight : float 
    married : bool
    allergies: Dict[str, str]
    contact_details: Dict[str,str]

    @field_validator('email', mode= 'after') #after here means after type coersion
    @classmethod
    def email_validator(cls, value):

        valid_domains = ['hdfc.com', 'icici.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1] 

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age', mode="after")
    @classmethod
    def valid_age(cls, value):
        if 0 < value < 100: 
            return value
        else:
            raise ValueError("Age shuld be in between 0 and 100")
    

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

patient_info = {"name": "Pravin","email": "abc@hdfc.com", "linkedin_url":"http://linkedin.com/1322", "age": 30, "weight": 75.2, "married": True,"allergies": {"Dust": "Yes"},  "contact_details":{"email": "abc@gmail.com", "phone": "15666545"}}

patient2 = Patient2(**patient_info) #Validation -> type coersion

insert_patient_data(patient2)
