from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    OPENAI_API_KEY: str
    model_config = SettingsConfigDict( env_file=".env", env_file_encoding="utf-8" )
    SECRET_KEY: str = "super-secret"
    COOKIE_NAME: str = "access_token"

settings = Settings()
