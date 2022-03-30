from pymongo import MongoClient
import os
from dotenv import load_dotenv
import requests
import time

load_dotenv()

# ============== Moscow data for Vk API ==============

# Coordinates of Red Square as the centre of Moscow
moscow_lat = 55.754045
moscow_long = 37.620538

# amount of results
count = 500

# Radius around Red Square
radius = 50000

# URL for loading photos
VK_PHOTOS_URL = \
    f"https://api.vk.com/method/photos.search?" \
    f"lat={moscow_lat}&long={moscow_long}&count={count}&radius={radius}&" \
    f"access_token={os.getenv('ACCESS_TOKEN')}&v=5.131"

city=1    # Moscow id
country=1 # Russia id
sex=1   # Women

VK_USER_URL = \
    f"https://api.vk.com/method/users.search?" \
    f"fields=about,activities,bdate,blacklisted,books,city,contacts,country,education,interests," \
    f"movies,music,nickname,relation,relatives,relatives,screen_name,sex,status,universities&" \
    f"city={city}&country={country}&sex={sex}&count={count}&" \
    f"access_token={os.getenv('ACCESS_TOKEN')}&v=5.131"


# Connect to MongoDb cluster
client = MongoClient(os.getenv('MONGO_CONNECTION_STRING'), connect=False)

# Use cluster database
db = client["vk_data"]

counter = 1
while True:
    photos_response = requests.get(VK_PHOTOS_URL)
    data = photos_response.json()["response"]["items"]
    documents = []
    for d in data:
        documents.append(d)

    user_response = requests.get(VK_USER_URL)
    user_data = user_response.json()["response"]["items"]
    users = []
    for user in user_data:
        users.append(user)

    db.photos.insert_many(documents)
    db.users.insert_many(users)
    print(counter)
    counter += 1

    time.sleep(1)

