from app.models.user import User
from app.database import SessionLocal

def check_balance(user_id: int) -> float:
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            return user.balance
        else:
            return 0.0  # В случае, если пользователь не найден

def deduct_credits(user_id: int, amount: float) -> bool:
    with SessionLocal() as db:
        user = db.query(User).filter(User.id == user_id).first()
        if user and user.balance >= amount:
            user.balance -= amount
            db.commit()
            return True
        return False
