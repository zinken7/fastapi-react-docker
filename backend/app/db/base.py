# -*- coding:utf-8 -*-
# Author: zinken7
# Copyright (c) 2021 - MTDT Services
# This file is use for commercial purpose only.
# -------------*-*-*--*-*-*--*-*-*------------


# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base
from app.models.user import User
