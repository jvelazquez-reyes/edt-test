from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config.config import SessionLocal
from sqlalchemy.orm import Session
from schemas.restaurant import RestaurantSchema, Request, Response, RequestRestaurant

# Import the controller where all the database transactions are performed
import controller.crud_restaurant 

# Instantiate the APIRouter class to define endpoints, handle request and params
router = APIRouter()

#Getting the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to make the POST request
@router.post("/create")
def create_restaurant_service(request: RequestRestaurant, db: Session = Depends(get_db)):
    # Calling the controller to perform the database transaction
    controller.crud_restaurant.create_restaurant(db, restaurant=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Restaurant created successfully").dict(exclude_none=True)


# Route to GET all restaurants
@router.get("/")
def get_restaurants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _restaurants = controller.crud_restaurant.get_restaurant(db, skip, limit)
    return Response(status="Ok", code="200", message="All restaurants fetched successfully", result=_restaurants)

# Route to update one restaurant information
@router.put("/update")
def update_restaurant(request: RequestRestaurant, db: Session = Depends(get_db)):
    _restaurant = controller.crud_restaurant.update_restaurant(db, restaurant_id=request.parameter.id,
                            rating=request.parameter.rating,
                            name=request.parameter.name,
                            site=request.parameter.site,
                            email=request.parameter.email,
                            phone=request.parameter.phone,
                            street=request.parameter.street,
                            city=request.parameter.city,
                            state=request.parameter.state,
                            lat=request.parameter.lat,
                            lng=request.parameter.lng
                             )
    return Response(status="Ok", code="200", message="Restaurant updated successfully", result=_restaurant)

# Route to DELETE one restaurant by restaurant_id
@router.delete("/delete")
def delete_restaurant(request: RequestRestaurant,  db: Session = Depends(get_db)):
    controller.crud_restaurant.remove_restaurant(db, restaurant_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Restaurant deleted successfully").dict(exclude_none=True)

# Route to perform the statistics (COUNT, AVERAGE, STDDEV)
@router.get("/statistics/")
def get_statistics(latitude: float, longitude: float, radius: float, db: Session = Depends(get_db)):
    # Calling the controller to perform the geospatial queries using Postgis
    _nearby_restaurants = controller.crud_restaurant.get_stats(db, latitude, longitude, radius)
    return Response(status="Ok", code="200", message="Some stats performed successfully", result=_nearby_restaurants)