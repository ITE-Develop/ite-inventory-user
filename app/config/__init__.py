from .connect_da import DB
class Config():
    DEBUG = True
    APP_NAME = "SCHOOOL MANAGEMENT SYSTEM"
    SECRET_KEY = b'ZbCW2oMkb9_gBZ_WKhIl7mtsQVHX7vjSuev9d83ipoI='
    SQLALCHEMY_DATABASE_URI = DB().postgres_uri()