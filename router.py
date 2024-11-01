from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskID

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)
@router.post("")
async def add_task2(
    task: Annotated[STaskAdd, Depends()],
) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def add_task() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks