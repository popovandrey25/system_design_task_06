import json
import os
from typing import List, Optional

from aiokafka import AIOKafkaProducer
from bson import ObjectId

from app.models import Route
from app.db import db


KAFKA_TOPIC = "routes-topic"
BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")


class RouteRepository:
    collection = db.routes

    def __init__(self):
        self.producer = AIOKafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)

    async def start(self):
        await self.producer.start()

    async def stop(self):
        await self.producer.stop()

    async def create_route(self, start: str, end: str, waypoints: list[str]) -> Route:
        route_id = str(ObjectId())
        event = {
            "type": "route_created",
            "payload": {
                "route_id": route_id,
                "start_point": start,
                "end_point": end,
                "waypoints": waypoints,
            }
        }
        await self.producer.send_and_wait(KAFKA_TOPIC, json.dumps(event).encode())
        return Route(route_id=route_id, start_point=start, end_point=end, waypoints=waypoints)

    @staticmethod
    async def get_route_by_id(route_id: str) -> Optional[Route]:
        doc = await RouteRepository.collection.find_one({"_id": ObjectId(route_id)})
        if not doc:
            return None
        return Route(
            route_id=str(doc["_id"]),
            start_point=doc["start_point"],
            end_point=doc["end_point"],
            waypoints=doc.get("waypoints", [])
        )

    @staticmethod
    async def get_all_routes() -> List[Route]:
        routes: List[Route] = []
        async for doc in RouteRepository.collection.find():
            routes.append(
                Route(
                    route_id=str(doc["_id"]),
                    start_point=doc["start_point"],
                    end_point=doc["end_point"],
                    waypoints=doc.get("waypoints", [])
                )
            )
        return routes

    @staticmethod
    async def find_routes(
        start_point: Optional[str] = None,
        end_point: Optional[str] = None,
    ) -> List[Route]:
        query: dict = {}
        if start_point:
            query["start_point"] = start_point
        if end_point:
            query["end_point"] = end_point

        routes: List[Route] = []
        async for doc in RouteRepository.collection.find(query):
            routes.append(
                Route(
                    route_id=str(doc["_id"]),
                    start_point=doc["start_point"],
                    end_point=doc["end_point"],
                    waypoints=doc.get("waypoints", []),
                )
            )
        return routes
