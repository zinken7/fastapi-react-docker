# -*- coding:utf-8 -*-
# Author: zinken7
# Copyright (c) 2021 - MTDT Services
# This file is use for commercial purpose only.
# -------------*-*-*--*-*-*--*-*-*------------


import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyUrl, AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, RedisDsn, PostgresDsn, validator


class Settings(BaseSettings):

    # General
    DOMAIN: str
    API_DOMAIN: str
    PROJECT_NAME: str
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = secrets.token_urlsafe(32)
    
    # User
    FIRST_SUPERUSER_EMAIL: EmailStr
    FIRST_SUPERUSER_PASSWORD: str
    FIRST_SUPERUSER_FIRSTNAME: str = "Superuser"
    FIRST_SUPERUSER_LASTNAME: str = "Superuser"
    SUPERUSER_ROLE: str
    SUPERUSER_DEPARTMENT: str
    USERS_OPEN_REGISTRATION: bool = False

    # API
    API_VERSION: str = "1"
    API_VERSION_STR = "/api/v{API_VERSION}"

    # Redis
    REDIS_HOST: Optional[str]
    REDIS_PASSWORD: str
    REDIS_DSN: str = 'redis://:{REDIS_PASSWORD}@{REDIS_SERVER}:6379/0'
    
    # RabbitMQ
    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str
    RABBITMQ_DEFAULT_VHOST: str
    RABBITMQ_DSN: AnyUrl = "amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@{RABBITMQ_SERVER}:5672/{RABBITMQ_DEFAULT_VHOST}"

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # Database
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()
