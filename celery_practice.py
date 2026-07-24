from celery import Celery 
from time import sleep
import time





app = Celery('tasks', broker="https://live-treefrog-179617.upstash.io",
             backend= "https://live-treefrog-179617.upstash.io"
             )

@app.task
def simulate_llm_call(prompt):
    time.sleep(10)
    return f"Response to : {prompt}"

