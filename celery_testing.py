from fastapi import FastAPI
from celery_practice import simulate_llm_call
from celery.result import AsyncResult

api = FastAPI()


@api.post("/process")
def process(prompt: str):
    task = simulate_llm_call.delay(prompt)
    return {"task_id": task.id}


@api.get("/status/{task_id}")
def status(task_id: str):
    result = AsyncResult(task_id)

    return {
        "status": result.status,
        "result": result.result if result.ready() else None
    }