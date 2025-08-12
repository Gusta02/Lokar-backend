from fastapi import FastAPI
from app.api import auth

app = FastAPI(title="Lokar Backend")

app.include_router(auth.router)

@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}
