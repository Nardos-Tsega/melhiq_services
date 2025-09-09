from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}   

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}