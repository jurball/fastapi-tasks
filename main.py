from typing import Optional, Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()

class STaskAdd(BaseModel): # сущность таски
    name: str
    description: Optional[str] = None # как необязательный

tasks = []

@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
):
    tasks.append(task)
    return { "ok": True }

@app.get("/tasks")
def get_tasks():
    return { "data": tasks }