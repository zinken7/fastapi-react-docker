# -*- coding:utf-8 -*-
# Author: zinken7
# Copyright (c) 2021 - MTDT Services
# This file is use for commercial purpose only.
# -------------*-*-*--*-*-*--*-*-*------------


from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None
    permissions: str = "user"