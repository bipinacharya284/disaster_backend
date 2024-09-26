from motor.motor_asyncio import AsyncIOMotorClient

class Database:
    def __init__(self):
        self.client = AsyncIOMotorClient("mongodb://localhost:27017")
        self.db = self.client["sensor_db"]

db = Database().db