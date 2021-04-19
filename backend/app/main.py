# -*- coding:utf-8 -*-
# Author: zinken7
# Copyright (c) 2021 - MTDT Services
# This file is use for commercial purpose only.
# -------------*-*-*--*-*-*--*-*-*------------


from fastapi import FastAPI, Depends

from app.core.config import settings
from app.core.auth import get_current_active_user
from app.core.celery import worker

from app.api.api_v1.routers.users import users_router
from app.api.api_v1.routers.auth import auth_router

from app import tasks


app = FastAPI(
    title=settings.PROJECT_NAME, docs_url="/api/docs", openapi_url="/api"
)


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/task")
async def example_task():
    worker.send_task("app.tasks.example_task", args=["Hello World"])

    return {"message": "success"}


# Routers
app.include_router(
    users_router,
    prefix="/api/v1",
    tags=["users"],
    dependencies=[Depends(get_current_active_user)],
)
app.include_router(auth_router, prefix="/api", tags=["auth"])