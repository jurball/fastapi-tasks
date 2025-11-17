from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel): # сущность таски
    name: str
    description: Optional[str] = None # как необязательный

@app.get("/tasks")
def get_tasks():
    task = Task(name="New Task")
    return { "data": task }