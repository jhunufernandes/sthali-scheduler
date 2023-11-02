from typing import Literal

import httpx
from fastapi import status, HTTPException


class API:
    servide: str
    timeout: int
    try_count: int

    def __init__(self, service: str, timeout: int = 10, try_count: int = 3) -> None:
        self.service = service
        self.timeout = timeout
        self.try_count = try_count

    def request(
        self,
        method: Literal["GET", "POST"],
        endpoint: str,
        headers: dict = {},
        body: dict = {},
        query: dict = {},
    ) -> dict:
        errors = []
        url = f"{self.service}/{endpoint}"
        for _ in range(self.try_count):
            try:
                response = httpx.request(
                    method,
                    url,
                    headers=headers,
                    json=body,
                    params=query,
                    timeout=self.timeout,
                )
                assert response.status_code == status.HTTP_200_OK
                return response.json()
            except Exception as exception:
                errors.append(repr(exception))
        raise HTTPException(500, errors)


def call(service: str, request_kwargs: dict) -> dict:
    client = API(service)
    client.request(**request_kwargs)
