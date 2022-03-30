from pymongo.database import Database
import requests
import time
from config import VK_USER_URL


def load_users_data(db: Database) -> None:
    """
    Load Moscow users data rrom Vk API.

    Args:
        db:
            mongo database.
    """
    while True:
        user_response = requests.get(VK_USER_URL)
        user_data = user_response.json()["response"]["items"]
        users = []
        for user in user_data:
            users.append(user)
        db.users.insert_many(users)
        
        time.sleep(1)
