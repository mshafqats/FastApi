from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str = "super-secret"
    COOKIE_NAME: str = "access_token"

settings = Settings()
