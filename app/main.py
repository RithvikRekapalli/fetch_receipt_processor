from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(
    title="Receipt-Processor API",
    version="1.0.0",
    description="Backend coding exercise for Fetch Rewards",
)

# All receipt-related routes
app.include_router(router)

# Root route – returns a simple JSON greeting and points users to /docs

@app.get("/", include_in_schema=False)
async def root():
    """
    Health / landing endpoint.
    Not included in the OpenAPI schema so that /docs stays clean.
    """
    return {"message": "Receipt-Processor API up and running. Visit /docs for Swagger UI."}
