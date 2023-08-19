from fastapi import FastAPI

http_service = FastAPI()

@http_service.get("/")
async def root():
    return {"message": "Trades bro"}
