from fastapi import FastAPI
from app.routers import order


app = FastAPI()

app.include_router(order.router)