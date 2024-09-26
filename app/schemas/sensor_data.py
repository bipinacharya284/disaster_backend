from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class SensorDataSchema(BaseModel):
    sensor_id: str
    value: float


class NodeMCUDataSchema(BaseModel):
    device_id: str
    sensor_data: List[SensorDataSchema]
    sent_at: Optional[datetime] = None

    class Config:
        orm_mode = True
