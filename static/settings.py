from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    BASE_URL: str = "https://playwright.dev/"
    BASE_TEST_STAND_URL: str = "https://api.test.profcomff.com/"

@lru_cache
def get_settings() -> Settings:
    return Settings()
