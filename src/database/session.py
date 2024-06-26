from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings

engine = create_async_engine(
    settings.database_url,
    echo=settings.DEBUG,
)

session_factory = async_sessionmaker(engine)
