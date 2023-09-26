from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setting up the database url
# Params required:
# - <user> postgres
# - <password> password
# - <host> localhost or db (Docker service for database)
# - <port> 5432
# - <database name> restaurant_db
DATABASE_URL = 'postgresql://postgres:password@db:5432/restaurant_db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()