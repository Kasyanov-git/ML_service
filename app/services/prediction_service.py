from rq import Queue
from redis import Redis
from app.workers import prediction_worker

# Параметры подключения к Redis
redis_url = "redis://localhost:6379"

# Подключение к Redis для работы с очередью задач
redis_conn = Redis.from_url(redis_url)
q = Queue(connection=redis_conn)

def create_prediction_task(user_id: int, input_data: dict) -> str:
    # Добавление задачи расчета в очередь RQ
    job = q.enqueue(prediction_worker.perform_prediction, user_id, input_data)
    return job.get_id()

