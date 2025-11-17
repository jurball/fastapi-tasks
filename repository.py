from sqlalchemy import select

from database import new_session, TaskOrm
from schemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int: # добавить таску
        async with new_session() as session: # менеджер сессии
            task_dict = data.model_dump() # превращаем в виде словаря

            task = TaskOrm(**task_dict) # создать таску
            session.add(task) # выполняем транзакцию
            await session.flush() # получит id
            await session.commit() # выполнить в БД

            return task.id

    @classmethod
    async def find_all(cls) -> list[STask]: # получить все таски
        async with new_session() as session: # менеджер сессии
            query = select(TaskOrm) # запрос
            result = await session.execute(query) # исполнить запрос
            task_models = result.scalars().all() # получить все объект итерации
            task_schemas = [STask.model_validate(task_model) for task_model in task_models] # валидировать каждую таску
            return task_schemas

