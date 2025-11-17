from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"] # для Swagger Doc
)

@router.post("") # эндпоинт для создания таски
async def add_task(
        task: Annotated[STaskAdd, Depends()] # валидация тасок
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return { "ok": True, "task_id": task_id }

@router.get("") # эндпоинт для получения всех тасок
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks