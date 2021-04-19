# -*- coding:utf-8 -*-
# Author: zinken7
# Copyright (c) 2021 - MTDT Services
# This file is use for commercial purpose only.
# -------------*-*-*--*-*-*--*-*-*------------


from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings
from app.lib.vi_en import convert


def init_db(db: Session) -> None:
    # Create 1st superuser
    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER_EMAIL)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER_EMAIL,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            first_name=settings.FIRST_SUPERUSER_FIRSTNAME,
            last_name=settings.FIRST_SUPERUSER_LASTNAME,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
