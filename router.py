from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd

router = APIRouter(
    prefix="/tasks",
)

@router.post("") # эндпоинт для создания таски
async def add_task(
        task: Annotated[STaskAdd, Depends()] # валидация тасок
):
    task_id = await TaskRepository.add_one(task)
    return { "ok": True, "task_id": task_id }

@router.get("") # эндпоинт для получения всех тасок
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return { "tasks": tasks }