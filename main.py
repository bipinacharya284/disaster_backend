from fastapi import FastAPI
from app.routes.sensor_route import router as sensor_router

app = FastAPI()

app.include_router(sensor_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
