from fastapi import APIRouter, Depends, HTTPException, status
from app.core.security import authenticate_user, create_access_token
from app.api.schemas.auth import Token, AuthForm

router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: AuthForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
