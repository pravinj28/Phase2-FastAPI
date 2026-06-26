def insert_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("inserted into database")
    else:
        raise TypeError('Incorrect data type')


insert_patient_data('pravin', 21)

def update_patient_data(name: str, age: int):
    if type(name) == str and type(age) == int:
        print(name)
        print(age)
        print("updated into database")
    else:
        raise TypeError('Incorrect data type')
