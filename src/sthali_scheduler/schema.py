from typing import Literal

from pydantic import BaseModel


class Call(BaseModel):
    body: dict
    endpoint: str
    method: Literal["GET", "POST"]
    service: str
    body: dict = {}
    headers: dict = {}
    query: dict = {}


class Response(BaseModel):
    detail: str
    status: int
