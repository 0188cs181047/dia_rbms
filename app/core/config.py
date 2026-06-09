from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "VendorSystem"

    # DB
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    DATABASE_URL: str

    # REDIS
    REDIS_URL: str

    # PGADMIN
    PGADMIN_EMAIL: str
    PGADMIN_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()