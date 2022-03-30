from pymongo.database import Database
import requests
import time
from config import VK_PHOTOS_URL


def load_photos_data(db: Database) -> None:
    """
    Load Moscow photos data rrom Vk API.

    Args:
        db:
            mongo database.
    """
    while True:
        photos_response = requests.get(VK_PHOTOS_URL)
        data = photos_response.json()["response"]["items"]
        documents = []
        for d in data:
            documents.append(d)


        db.photos.insert_many(documents)

        time.sleep(1)
