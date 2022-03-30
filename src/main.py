from photos import load_photos_data
from users import load_users_data
from db import get_db, get_client


if __name__ == "__main__":
    client = get_client()
    db = get_db(client)

    load_photos_data(db)
    load_users_data(db)
