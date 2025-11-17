from typing import Annotated

from fastapi import FastAPI, Depends

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI): # жизненный цикл приложения
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к использованию")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan) # создать экземпляр FastAPI
app.include_router(tasks_router) # подключить роут