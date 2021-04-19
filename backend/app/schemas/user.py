# -*- coding:utf-8 -*-
# Author: zinken7
# Copyright (c) 2021 - MTDT Services
# This file is use for commercial purpose only.
# -------------*-*-*--*-*-*--*-*-*------------


from typing import Optional
from pydantic import BaseModel, EmailStr


# Base properties
class UserBase(BaseModel):
    email: EmailStr = None

    first_name: str = None
    last_name: str = None

    is_active: bool = True
    is_superuser: bool = False

# Get User
class UserOut(UserBase):
    pass

# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True


# Properties to receive via API on edit
class UserEdit(UserBase):
    email: Optional[EmailStr] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True


# User in db
class User(UserBase):
    id: int

    class Config:
        orm_mode = True
