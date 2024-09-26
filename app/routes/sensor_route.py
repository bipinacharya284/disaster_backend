from fastapi import APIRouter, HTTPException
from app.schemas.sensor_data import NodeMCUDataSchema
from app.services.sensor_service import SensorService


router = APIRouter()


@router.post("/sensor-data")
async def receive_sensor_data(data: NodeMCUDataSchema):
    try:
        stored_data = await SensorService.save_sensor_data(
            data.device_id, data.sensor_data, data.sent_at
        )
        return {"message": "Data saved successfully", "data": stored_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sensor-data/{sensor_id}")
async def get_sensor_data(sensor_id: str):
    try:
        data = await SensorService.get_all_sensor_data(sensor_id)
        return {"data": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
