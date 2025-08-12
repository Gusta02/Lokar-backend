from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import UserCreate, Token
from app.services.auth_service import register_user, authenticate_user, create_token_for_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserCreate)
async def register(user: UserCreate):
    created = register_user(user.email, user.password)
    if not created:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    return created

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_token_for_user(user)
    return {"access_token": token, "token_type": "bearer"}
