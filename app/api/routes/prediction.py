from fastapi import APIRouter, Depends, BackgroundTasks
from app.services.prediction_service import create_prediction_task

router = APIRouter()

@router.post("/create")
async def create_prediction(user_id: str, background_tasks: BackgroundTasks):
    # Здесь должна быть логика создания задачи на расчет предсказания
    task_id = create_prediction_task(user_id)
    background_tasks.add_task(task_id)
    return {"task_id": task_id}
