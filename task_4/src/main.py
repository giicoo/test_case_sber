from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.core.database import connect_to_db, close_db_connection
from src.api.v1 import main_router
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    session = await connect_to_db()
    app.state.db_session = session
    yield 
    await close_db_connection(session)

app = FastAPI(
    title="URL Shortener API",
    lifespan=lifespan
)

app.include_router(main_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)