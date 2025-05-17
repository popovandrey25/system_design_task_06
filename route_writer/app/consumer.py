import asyncio
import json
import logging
import os

from aiokafka import AIOKafkaConsumer
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient


KAFKA_TOPIC = "routes-topic"
BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
MONGO_URL = os.getenv("MONGODB_URL")
MONGO_DB  = os.getenv("MONGODB_DB")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)


async def consume():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=BOOTSTRAP_SERVERS,
        group_id="route-writer-group",
        auto_offset_reset="earliest"
    )
    await consumer.start()

    mongo = AsyncIOMotorClient(MONGO_URL)[MONGO_DB]
    try:
        async for msg in consumer:
            event = json.loads(msg.value)
            if event.get("type") == "route_created":
                p = event["payload"]
                # сохраняем в коллекцию routes
                await mongo.routes.insert_one({
                    "_id": ObjectId(p["route_id"]),
                    "start_point": p["start_point"],
                    "end_point": p["end_point"],
                    "waypoints": p["waypoints"]
                })
                logger.info(f"Route {p['route_id']} written to Mongo")
    finally:
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(consume())
