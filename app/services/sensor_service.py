from typing import List
from app.models.sensor_data import SensorDataModel, NodeMCUDataModel
from app.core.database import db
from datetime import datetime


class SensorService:
    @staticmethod
    async def save_sensor_data(
        device_id: str, sensor_data: list, sent_at: datetime = None
    ) -> NodeMCUDataModel:
        received_at = datetime.utcnow()
        stored_data = []

        for sensor in sensor_data:
            data = {
                "sensor_id": sensor.sensor_id,
                "value": sensor.value,
                "sent_at": sent_at or received_at,
                "received_at": received_at,
            }

            collection_name = f"sensor{sensor.sensor_id}"
            result = await db[collection_name].insert_one(data)
            created_data = await db[collection_name].find_one(
                {"_id": result.inserted_id}
            )
            created_data["id"] = created_data.pop("_id")
            stored_data.append(SensorDataModel(**created_data))

        return NodeMCUDataModel(
            id=None,
            device_id=device_id,
            sensor_data=stored_data,
            sent_at=sent_at or received_at,
            received_at=received_at,
        )

    @staticmethod
    async def get_all_sensor_data(sensor_id: str) -> List[SensorDataModel]:
        collection_name = f"sensor{sensor_id}"
        sensor_data = await db[collection_name].find().to_list(100)

        # Convert ObjectId to PyObjectId to avoid issues during serialization
        return [SensorDataModel(**{**data, "id": data["_id"]}) for data in sensor_data]
