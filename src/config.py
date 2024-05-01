from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_CONTAINER_PORT: int
    POSTGRES_DB: str

    @property
    def database_url(self) -> str:
        """Return PostgreSQL connection string."""
        return PostgresDsn.build(
            scheme='postgresql+asyncpg',
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_CONTAINER_PORT,
            path=self.POSTGRES_DB,
        ).unicode_string()


settings = Settings()
