from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(
    title="Fetch Receipt Processor",
    version="1.0.0",
    description="Backend coding exercise for Fetch Rewards"
)

app.include_router(router)
