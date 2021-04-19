# -*- coding:utf-8 -*-
# Author: zinken7
# Copyright (c) 2021 - MTDT Services
# This file is use for commercial purpose only.
# -------------*-*-*--*-*-*--*-*-*------------


from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Boolean, Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class User(Base):
    id              = Column(Integer, primary_key=True, index=True)
    email           = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name      = Column(String)
    last_name       = Column(String)
    is_active       = Column(Boolean(), default=True)
    is_superuser    = Column(Boolean(), default=False)
    created_at      = Column(DateTime, default=func.now())
