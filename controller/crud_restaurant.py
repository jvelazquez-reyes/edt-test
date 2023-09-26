from sqlalchemy.orm import Session
from sqlalchemy import text
from models.restaurant import Restaurant
from schemas.restaurant import RestaurantSchema

from config.config import engine


# Query to get all restaurant in database
def get_restaurant(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Restaurant).offset(skip).limit(limit).all()

# Query to get restaurant by id
def get_restaurant_by_id(db: Session, restaurant_id: str):
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

# Query to create a new restaurant
def create_restaurant(db: Session, restaurant: RestaurantSchema):
    _restaurant = Restaurant(
        id=restaurant.id,
        rating=restaurant.rating,
        name=restaurant.name,
        site=restaurant.site,
        email=restaurant.email,
        phone=restaurant.phone,
        street=restaurant.street,
        city=restaurant.city,
        state=restaurant.state,
        lat=restaurant.lat,
        lng=restaurant.lng
    )
    db.add(_restaurant)
    db.commit()
    db.refresh(_restaurant)
    return _restaurant

# Query to delete a restaurant
def remove_restaurant(db: Session, restaurant_id: str):
    _restaurant = get_restaurant_by_id(db=db, restaurant_id=restaurant_id)
    db.delete(_restaurant)
    db.commit()

# Query to update an existing restaurant. Data is fetched by restaurant_id
def update_restaurant(
        db: Session,
        restaurant_id: str,
        rating: int, 
        name: str,
        site: str,
        email: str,
        phone: str,
        street: str,
        city: str,
        state: str,
        lat: float,
        lng: float
    ):
    _restaurant = get_restaurant_by_id(db=db, restaurant_id=restaurant_id)

    _restaurant.rating = rating
    _restaurant.name = name
    _restaurant.site = site
    _restaurant.email = email
    _restaurant.phone = phone
    _restaurant.street = street
    _restaurant.city = city
    _restaurant.state = state
    _restaurant.lat = lat
    _restaurant.lng = lng

    db.commit()
    db.refresh(_restaurant)
    return _restaurant

# Raw SQL queries to perform the stats
# These queries are made using Postgis
def get_stats(db: Session, latitude: float, longitude: float, radius: float):
    # Count
    # The ST_Distance is converted from miles to meters: the conversion factor is 0.000621371
    count_statement = f"""SELECT COUNT(rating) FROM restaurant where ST_Distance('POINT(:lng :lat)'::geography, ST_MakePoint(lng,lat)) * 0.000621371 <= :radius;"""
    # Average
    avg_statement = f"""SELECT AVG(rating) FROM restaurant where ST_Distance('POINT(:lng :lat)'::geography, ST_MakePoint(lng,lat)) * 0.000621371 <= :radius;"""
    # Standard deviation
    std_statement = f"""SELECT STDDEV(rating) FROM restaurant where ST_Distance('POINT(:lng :lat)'::geography, ST_MakePoint(lng,lat)) * 0.000621371 <= :radius;"""


    with engine.begin() as conn:
        count_restaurants = conn.execute(text(count_statement), 
                                        {'lat': latitude,
                                         'lng': longitude,
                                         'radius': radius}).all()
        
        avg_rating = conn.execute(text(avg_statement), 
                                        {'lat': latitude,
                                         'lng': longitude,
                                         'radius': radius}).all()
        
        std_rating = conn.execute(text(std_statement), 
                                        {'lat': latitude,
                                         'lng': longitude,
                                         'radius': radius}).all()

        # Mapping the row-like sqlalchemy structure to dict in Python
        stats = [count_restaurants, avg_rating, std_rating]
        result = []
        get_count = [dict(x._mapping) for x in count_restaurants]
        get_avg = [dict(x._mapping) for x in avg_rating]
        get_std = [dict(x._mapping) for x in std_rating]

        print(get_count[0])

        result.append(get_count[0])
        result.append(get_avg[0])
        result.append(get_std[0])

    return result