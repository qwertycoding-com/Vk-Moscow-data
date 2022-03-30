from dotenv import load_dotenv
import os

load_dotenv()

# Coordinates of Red Square as the centre of Moscow
MOSCOW_LAT = 55.754045
MOSCOW_LONG = 37.620538

# amount of results
COUNT = 500

# Radius around Red Square
RADIUS = 50000

# amount of results
COUNT = 500

CITY=1    # Moscow id
COUNTRY=1 # Russia id
SEX=1   # Women

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
MONGO_CONNECTION_STRING = os.getenv('MONGO_CONNECTION_STRING')

# URL for loading photos
VK_PHOTOS_URL = (
    f"https://api.vk.com/method/photos.search?"
    f"lat={MOSCOW_LAT}&long={MOSCOW_LONG}&count={COUNT}&radius={RADIUS}&"
    f"access_token={ACCESS_TOKEN}&v=5.131"
)

# URL for loading users
VK_USER_URL = (
    f"https://api.vk.com/method/users.search?"
    f"fields=about,activities,bdate,blacklisted,books,city,contacts,country,education,interests,"
    f"movies,music,nickname,relation,relatives,relatives,screen_name,sex,status,universities&"
    f"city={CITY}&country={COUNTRY}&sex={SEX}&count={COUNT}&"
    f"access_token={ACCESS_TOKEN}&v=5.131"
)
