# -*- coding:utf-8 -*-
# Author: zinken7
# Copyright (c) 2021 - MTDT Services
# This file is use for commercial purpose only.
# -------------*-*-*--*-*-*--*-*-*------------


from celery import Celery
from config import settings

message_broker = f"amqp://{settings.RABBITMQ_DEFAULT_USER}:{settings.RABBITMQ_DEFAULT_PASS}@queue:5672/{settings.RABBITMQ_DEFAULT_VHOST}"

worker = Celery("worker", broker=message_broker)

worker.conf.task_routes = {"app.tasks.*": "main-queue"}