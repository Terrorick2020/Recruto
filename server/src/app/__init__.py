from fastapi import FastAPI

from .home.home_routes import router as home_router


app = FastAPI()

app.include_router( home_router )
