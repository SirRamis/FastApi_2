from dotenv import load_dotenv
from fastapi import FastAPI
from contextlib import asynccontextmanager

from sqlalchemy import create_engine, text

from connector.decorator_connector import db_url_creator
from database import create_tables, delete_tables
from router import router as tasks_router




@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(
    lifespan=lifespan,
    title="Martin Pozishn",
)
app.include_router(tasks_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}

