from urllib.parse import quote_plus
from os.path import dirname, abspath,join
from sqlalchemy import create_engine, URL
BASEDIR = abspath(dirname(dirname(__file__)))
class DB:
    def postgres_uri(self):
        dialect = 'postgresql'
        host = '172.18.0.2'
        db = 'api_db'
        user = 'admin'
        port = '5433'
        password = 'dbApi@2024!'
        db_uri = f'{dialect}://{user}:{quote_plus(password)}@{host}:{port}/{db}'
        return db_uri
    
    def postgres_connector_uri(self):
        url_object = URL.create(
                "postgresql+pg8000",
                username="admin",
                password="dbApi@2024!", 
                host="172.18.0.2",
                database="api_db",
            )
        engine = create_engine(url_object)
        
        return engine
    
    def mysql_uri(self):
        dialect = 'mysql'
        host = 'mysql.cjyu2g4g0pi9.ap-southeast-1.rds.amazonaws.com'
        db = 'smsdb'
        user = 'admin'
        port = '3306'
        password = 'Rupp2357.!'
        db_uri = f'{dialect}://{user}:{quote_plus(password)}@{host}:{port}/{db}'
        return db_uri
    
    def mysql_connector_uri(self):
        dialect = 'mysql+mysqlconnector'
        host = 'mysql.cjyu2g4g0pi9.ap-southeast-1.rds.amazonaws.com'
        db = 'smsdb'
        user = 'admin'
        port = '3306'
        password = 'Rupp2357.!'
        db_uri = f'{dialect}://{user}:{quote_plus(password)}@{host}:{port}/{db}'
        return db_uri

    def redis_uri(self):
        dialect = 'redis'
        host = ''
        db = ''
        port = ''
        password = ''
        return f'{dialect}://:{password}@{host}:{port}/{db}'

    def sqlite_uri(self):
        db_path = join(BASEDIR,'data', 'smsdb.db')
        return f'sqlite:///{db_path}'