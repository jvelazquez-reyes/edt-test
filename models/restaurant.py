from sqlalchemy import  Column, Integer, String, Float
from config.config import Base

# Defining the model
class Restaurant(Base):
    # Naming the table in the restaurant_db database
    __tablename__ ="restaurant"

    # Field for the restaurant table
    id = Column(String, primary_key=True)
    rating = Column(Integer)
    name = Column(String)
    site = Column(String)
    email = Column(String)
    phone = Column(String)
    street = Column(String)
    city = Column(String)
    state = Column(String)
    lat = Column(Float)
    lng = Column(Float)