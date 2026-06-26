from fastapi import FastAPI

print("Running demo_project.py")


app = FastAPI() #app is the object which is the object of fastapi, creates the FASTAPI application object entry point of your entire API

@app.get("/") #This is a decorator — it tells FastAPI "when someone makes a GET request to this URL, run the function below it."
                 #For endpoints you have to define routes, get signifies request will be get,kisi server se data dekhna chahte ho toh get use karte ho
def hello():
    return {'message': "Hello world"}     #this is the method

@app.get('/about')
def about():
    return {'message': 'Campusx is an education platform where you can learn AI'}
