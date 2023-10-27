FROM python:3.11.0-alpine AS base

LABEL maintainer="Jhunu Fernandes jhunu.fernandes@gmail.com"

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN apk add --no-cache build-base libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-base libffi-dev openssl-dev

FROM base AS final

COPY ./src /app/src

ENTRYPOINT ["uvicorn", "src.run:app", "--host", "0.0.0.0", "--port", "80"]

EXPOSE 80
