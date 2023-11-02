from fastapi import FastAPI
from sthali_crud import AppSpecification, SthaliCRUD

from .config import lifespan


class SthaliScheduler:
    app: FastAPI

    def __init__(self, app_spec: AppSpecification) -> None:
        sthali_crud = SthaliCRUD(app_spec, lifespan)
        self.app = sthali_crud.app
