from datetime import timedelta
from app.core.security import hash_password, verify_password, create_access_token
from app.storage.user_storage import users_db, user_id_seq

def register_user(email: str, password: str):
    global user_id_seq
    if email in users_db:
        return None  # usuário já existe
    hashed = hash_password(password)
    users_db[email] = {"id": user_id_seq, "email": email, "hashed_password": hashed}
    user_id_seq += 1
    return users_db[email]

def authenticate_user(email: str, password: str):
    user = users_db.get(email)
    if not user or not verify_password(password, user["hashed_password"]):
        return None
    return user

def create_token_for_user(user):
    data = {"sub": user["email"], "id": user["id"]}
    return create_access_token(data)
