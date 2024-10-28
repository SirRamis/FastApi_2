from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router

# def fake_answer_to_everything_ml_model(x: float):
#     return x * 42


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
    title="Martin Pozishn"
)
app.include_router(tasks_router)
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
