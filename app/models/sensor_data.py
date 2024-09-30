from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime
from typing import List, Optional


# Custom ObjectId type for Pydantic
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object id")
        return v  # Return the original value to avoid conflicts


# Model for individual sensor data
class SensorDataModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    sensor_id: str
    value: float
    sent_at: datetime
    received_at: datetime

    class Config:
        json_encoders = {PyObjectId: lambda v: str(v)}  # Serialize as string


# Model for the NodeMCU data
class NodeMCUDataModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    device_id: str
    sensor_data: List[SensorDataModel]
    sent_at: Optional[datetime] = None
    received_at: Optional[datetime] = Field(
        default_factory=datetime.now
    )  # Optional to allow missing fields

    class Config:
        json_encoders = {PyObjectId: lambda v: str(v)}  # Serialize as string
