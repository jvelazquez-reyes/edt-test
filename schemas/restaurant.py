from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel , Field
from pydantic.generics import GenericModel

# Reference to a type variable
T = TypeVar('T')

# Defining the constraints of the fields for the Restaurant model
class RestaurantSchema(BaseModel):
    id: Optional[str] = None
    rating: Optional[int] = None
    name: Optional[str] = None
    site: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None

    class Config:
        orm_mode = True

# Validate the request
class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)

#Validate the request schema of the Restaurant model
class RequestRestaurant(BaseModel):
    parameter: RestaurantSchema = Field(...)

# Defining the types and constraints of the output
class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]