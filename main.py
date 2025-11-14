from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

import auth
import models
import schemas
from models import get_db

app = FastAPI()

@app.post("/token")
def login_for_access_token(
    login_data: schemas.LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.query(models.Usuario).filter(
        models.Usuario.login == login_data.username
    ).first()

    if not user or not auth.verify_password(login_data.password, user.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Login ou Senha incorretos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.login}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint "Hello World" (agora protegido)
@app.get("/users/me")
def read_users_me(current_user: schemas.Usuario = Depends(auth.get_current_user)):
    # Se chegar aqui, o usuário está logado.
    # A função get_current_user cuida da validação do token.
    return current_user