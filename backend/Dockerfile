FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

RUN apt update && \
    apt install -y postgresql-client

RUN pip install --upgrade pip

COPY requirements.txt ./

# install dependencies 
RUN pip install -r requirements.txt

COPY . .

# expose 8888 on container
EXPOSE 8888

ENV PORT=8888

ENV LOG_LEVEL=warning
