from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.database.session import engine

from . import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)


@app.get('/')
def read_root():
    return {'message': 'Taimu time!'}
