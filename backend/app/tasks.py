# -*- coding:utf-8 -*-
# Author: zinken7
# Copyright (c) 2021 - MTDT Services
# This file is use for commercial purpose only.
# -------------*-*-*--*-*-*--*-*-*------------


from app.core.celery import worker


@worker.task(acks_late=True)
def example_task(word: str) -> str:
    return f"test task returns {word}"
