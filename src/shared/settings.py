from pydantic_settings import BaseSettings
from typing import List, AnyHttpUrl


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:5173",
        "https://translation-service-app.herokuapp.com",
    ]
