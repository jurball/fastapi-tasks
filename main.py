from typing import Annotated

from fastapi import FastAPI, Depends

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from schemas import STaskAdd


@asynccontextmanager
async def lifespan(app: FastAPI): # жизненный цикл приложения
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к использованию")
    yield
    print("Выключение")

app = FastAPI(lefispan=lifespan)

tasks = []

@app.post("/tasks") # эндпоинт для создания таски
async def add_task(
        task: Annotated[STaskAdd, Depends()] # валидация тасок
):
    tasks.append(task)
    return { "ok": True }

@app.get("/tasks") # эндпоинт для получения всех тасок
def get_tasks():
    return { "data": tasks }