from fastapi import FastAPI
from os import path
from time import sleep
from uuid import UUID

from apscheduler.schedulers.background import BackgroundScheduler
from sthali_crud import AppSpecification, SthaliCRUD

from .api import API
from .config import get_schedules
from .schema import Call, Response

TINYDB_PATH = path.join(path.dirname(__file__), "../tinydb.json")
SPEC = {
    "resources": [
        {
            "db": {"engine": "tinydb", "path": TINYDB_PATH},
            "name": "runs",
            "fields": [
                {
                    "name": "schedule_id",
                    "type": UUID,
                },
                {
                    "name": "timestamp",
                    "type": str,
                },
                {
                    "name": "service",
                    "type": str,
                },
                {
                    "name": "endpoint",
                    "type": str,
                },
                {
                    "name": "method",
                    "type": str,
                },
                {
                    "name": "headers",
                    "type": dict,
                },
                {
                    "name": "body",
                    "type": dict,
                },
                {
                    "name": "query",
                    "type": dict,
                },
                {
                    "name": "status",
                    "type": int,
                },
                {
                    "name": "error_detail",
                    "type": str,
                    "default_value": None,
                    "has_default": True,
                },
            ],
        },
        {
            "db": {"engine": "tinydb", "path": TINYDB_PATH},
            "name": "schedules",
            "fields": [
                {
                    "name": "name",
                    "type": str,
                },
                {
                    "name": "fur",
                    "type": bool,
                },
            ],
        },
    ]
}


async def lifespan(app: FastAPI):
    print('sthali scheduler')
    yield
    print('sthali scheduler')


sthali_crud = SthaliCRUD(AppSpecification(**SPEC), lifespan)
app = sthali_crud.app


# schedules = get_schedules(sthali_crud)
# for schedule in schedules:
#     print(schedule)

# scheduler = BackgroundScheduler()


# def myfunc():
#     print("xxx")


# job = scheduler.add_job(myfunc, "interval", seconds=10)
# scheduler.start()

# @app.post("/{schedule_id}")
# async def get(schedule_id: UUID):
#     pass


# @app.post("/")
# async def call(payload: Call) -> Response:
#     client = API(payload.service)
#     return await client.call(
#         payload.method,
#         payload.endpoint,
#         headers=payload.headers,
#         body=payload.body,
#         query=payload.query,
#     )
