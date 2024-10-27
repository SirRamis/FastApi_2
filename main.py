from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Martin Pozishn"
)


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int



tasks = []
@app.post("/tasks")
async def add_task(
    task: STaskAdd,
):
    tasks.append(task)
    return {"ok": True}


