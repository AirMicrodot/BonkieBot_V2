# How to connect to a PostgreSQL database using python & sqlalchemy

from scqlalchemy import create_engine
import dataset

# dialect+driver://username:password@host:port/database
dialect = 'postgresql'
driver = 'pg8000'
username = 'sysadmin'
password = 'flipper'
host = 'localhost'
port = '5432'
database = 'kenamju'
baseStr = "{}+{}://{}:{}@{}:{}/{}"
engineStr = baseStr.format(dialect, driver, username, password, host, port, database)
print(engineStr)
db = dataset.connect(engineStr)
