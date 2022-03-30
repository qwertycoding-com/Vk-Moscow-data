from pymongo import MongoClient
from pymongo.database import Database
import os

def get_client() -> MongoClient:
    """
    Get user mongo client.
    """
    # Connect to MongoDb cluster
    client = MongoClient(os.getenv('MONGO_CONNECTION_STRING'), connect=False)
    return client


def get_db(client: MongoClient) -> Database:
    """
    Get mongo database.
    """
    db = client["vk_data"]
    return db
