# -*- coding:utf-8 -*-
# Author: zinken7
# Copyright (c) 2021 - MTDT Services
# This file is use for commercial purpose only.
# -------------*-*-*--*-*-*--*-*-*------------


from unidecode import unidecode

def convert(text):
    return unidecode(text).lower().replace(" ", "")