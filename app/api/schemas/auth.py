from pydantic import BaseModel

# Схема для входных данных аутентификации
class AuthForm(BaseModel):
    username: str
    password: str

# Схема для токена, который будет возвращаться после аутентификации
class Token(BaseModel):
    access_token: str
    token_type: str
