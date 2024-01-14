import time
from rq import get_current_job
from app.database import SessionLocal
from app.models.prediction import Prediction

def perform_prediction(user_id, input_data):
    job = get_current_job()
    print(f"Начало задачи: {job.id}")

    # Эмуляция вычислительно затратной операции
    time.sleep(10)
    result = "Результат предсказания"

    # Запись результата в базу данных
    db = SessionLocal()
    prediction = Prediction(user_id=user_id, result=result, cost=1.0)
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    db.close()

    print(f"Задача {job.id} завершена")
    return result
