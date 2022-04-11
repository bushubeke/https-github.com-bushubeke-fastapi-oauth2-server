
# import secrets
# from typing import Any, Dict, List, Optional, Union

# from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
from pydantic import BaseSettings 


class Settings(BaseSettings):
    #email settings to be filled
    # SMTP_TLS: bool = True
    # SMTP_PORT: Optional[int] = None
    # SMTP_HOST: Optional[str] = None
    # SMTP_USER: Optional[str] = None
    # SMTP_PASSWORD: Optional[str] = None
    # EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    # EMAILS_FROM_NAME: Optional[str] = None

    # database settings
    # DATABASE_MIGRATION_URI = 'postgresql+psycopg2://postgres:yahweh@192.168.10.5:5432/development-template'
    # DATABASE_ASYNC_URI='postgresql+asyncpg://postgres:yahweh@192.168.10.5:5432/development-template'
    DATABASE_MIGRATION_URI = "postgresql+a+psycopg2://ubfhbmrwbrnyhr:118dceefe549aba2517dd0ce5a2074a6508f0762c261fcf5039989a2a4056591@ec2-52-21-136-176.compute-1.amazonaws.com:5432/d1f5i526gppcpa"
    DATABASE_ASYNC_URI="postgresql+asyncpg://ubfhbmrwbrnyhr:118dceefe549aba2517dd0ce5a2074a6508f0762c261fcf5039989a2a4056591@ec2-52-21-136-176.compute-1.amazonaws.com:5432/d1f5i526gppcpa"

    

    class Config:
        case_sensitive = True


settings = Settings()