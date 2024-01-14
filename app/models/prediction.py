from sqlalchemy import Column, Integer, String, Float
from app.database import Base

# Модель для хранения предсказаний
class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    result = Column(String)
    cost = Column(Float)