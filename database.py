from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column

engine = create_async_engine( # асинхронный движок для работы с БД
    "sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(engine, expire_on_commit=False) # открытие транзакции БД

class Model(DeclarativeBase):
    pass

class TaskOrm(Model): # Объект модели
    __tablename__ = "tasks" # имя таблицы

    id: Mapped[int] = mapped_column(primary_key=True) # первичный ключ
    name: Mapped[str]
    description: Mapped[Optional[str]]

async def create_tables(): # функция для создания таблиц
    async with engine.begin() as conn: # обращаться к engine
        await conn.run_sync(Model.metadata.create_all) # создает все таблицы

async def delete_tables(): # функция для удаления всех таблиц
    async with engine.begin() as conn: # обращаться к engine
        await conn.run_sync(Model.metadata.drop_all) # создает все таблицы
