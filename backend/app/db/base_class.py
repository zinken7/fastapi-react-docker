# -*- coding:utf-8 -*-
# Author: zinken7
# Copyright (c) 2021 - MTDT Services
# This file is use for commercial purpose only.
# -------------*-*-*--*-*-*--*-*-*------------


from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
