from sqlalchemy import create_engine, URL

url_object = URL.create(
    "postgresql+pg8000",
    username="admin",
    password="dbApi@2024!", 
    host="172.18.0.2",
    database="api_db",
)
engine = create_engine(url_object)
print(engine)