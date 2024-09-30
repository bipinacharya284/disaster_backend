from fastapi import FastAPI
from app.routes.sensor_route import router as sensor_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(sensor_router, prefix="/api")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
