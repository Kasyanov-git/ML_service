from fastapi import APIRouter
from app.api.routes import auth, billing, prediction

router = APIRouter()

router.include_router(auth.router, tags=["Авторизация"], prefix="/auth")
router.include_router(billing.router, tags=["Биллинг"], prefix="/billing")
router.include_router(prediction.router, tags=["Предсказание"], prefix="/predict")
