from typing import List, Optional
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
        sensor_data = await db[collection_name].find().to_list()

        # Create SensorDataModel instances while ensuring proper ObjectId handling
        return [
            SensorDataModel(
                id=data["_id"],  # Directly assign _id to id
                sensor_id=data["sensor_id"],
                value=data["value"],
                sent_at=data["sent_at"],
                received_at=data["received_at"],
            )
            for data in sensor_data
        ]

    @staticmethod
    async def get_sensor_data_between(
        sensor_id: str, start_time: Optional[str] = None, end_time: Optional[str] = None
    ) -> List[SensorDataModel]:
        collection_name = f"sensor{sensor_id}"

        query_filter = {}

        if start_time:
            start_dt = datetime.fromisoformat(start_time)
            query_filter["received_at"] = {"$gte": start_dt}

        if end_time:
            end_dt = datetime.fromisoformat(end_time)
            if "received_at" in query_filter:
                query_filter["received_at"]["$lte"] = end_dt
            else:
                query_filter["received_at"] = {"$lte": end_dt}

        # Filter data between the given timestamps
        sensor_data = await db[collection_name].find(query_filter).to_list()

        # Create SensorDataModel instances while ensuring proper ObjectId handling
        return [
            SensorDataModel(
                id=data["_id"],  # Directly assign _id to id
                sensor_id=data["sensor_id"],
                value=data["value"],
                sent_at=data["sent_at"],
                received_at=data["received_at"],
            )
            for data in sensor_data
        ]
