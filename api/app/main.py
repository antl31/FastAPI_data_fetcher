from api.app import config
from api.app.routes import book

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


settings = config.get_settings()

app = FastAPI(
    title="Outflink test API",
    description="Outflink test API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(
    book.router,
    prefix="/api/book",
    tags=["Book"],
    responses={404: {"description": "Not found"}},
)
