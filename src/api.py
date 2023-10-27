from typing import Literal

import httpx
from fastapi import status


class API:
    servide: str
    timeout: int = 10

    def __init__(self, service: str) -> None:
        self.service = service

    def call(
        self,
        method: Literal["GET", "POST"],
        endpoint: str,
        headers: dict = {},
        body: dict = {},
        query: dict = {},
    ) -> dict:
        try:
            response = httpx.request(
                method,
                endpoint,
                headers=headers,
                json=body,
                params=query,
                timeout=self.timeout,
            )
            assert response.status_code == status.HTTP_200_OK
        except Exception as exception:
            breakpoint()
        else:
            return response.json()
