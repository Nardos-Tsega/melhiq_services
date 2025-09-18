from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="Melhiq main backend", version="1.0.0")

base_prefix = "/api/v1"

app.include_router(users.router, prefix=base_prefix + "/users", tags=["users"])

@app.get("/")
async def read_root():
    return {"Hello": "World"}   

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}