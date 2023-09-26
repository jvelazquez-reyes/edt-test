from fastapi import FastAPI
import models.restaurant
from routes.restaurant import router
from config.config import engine

# Create table objects of restaurant's metadata
models.restaurant.Base.metadata.create_all(bind=engine)

# Instantiate app
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello EDT Test"}

app.include_router(router, prefix="/restaurant", tags=["restaurant"])