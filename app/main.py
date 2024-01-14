from fastapi import FastAPI
from app.api.route import router as api_router

app = FastAPI()

# Включаем роутер с API маршрутами
app.include_router(api_router)
