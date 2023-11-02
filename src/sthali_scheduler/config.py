from contextlib import asynccontextmanager

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI

from .api import call


scheduler = AsyncIOScheduler()


async def get_schedules(app: FastAPI) -> list:
    print("Get schedules")
    return [
        {
            "id": schedule["id"],
            "scheduler_kwargs": {
                "minute": schedule["minute"],
                "hour": schedule["hour"],
                "day": schedule["day_of_month"],
                "month": schedule["month"],
                "day_of_week": schedule["day_of_week"],
            },
            "api_kwargs": {
                "service": schedule["service"],
                "request_kwargs": {
                    "endpoint": schedule["endpoint"],
                    "method": schedule["method"],
                    "headers": schedule["headers"],
                    "body": schedule["body"],
                    "query": schedule["query"],
                },
            },
        }
        for schedule in await app.extra["db"]["schedules"].read_all()
    ]


async def sync_scheduler(app: FastAPI, replace_existing: bool = False) -> None:
    print("Sync Scheduler")
    for schedule in await get_schedules(app):
        scheduler.add_job(
            id=schedule["id"],
            func=call,
            trigger="cron",
            kwargs=schedule["api_kwargs"],
            replace_existing=replace_existing,
            **schedule["scheduler_kwargs"],
        )


async def setup_scheduler(app: FastAPI) -> None:
    print("Setup Scheduler")
    await sync_scheduler(app)
    scheduler.add_job(
        sync_scheduler,
        "interval",
        minutes=1,
        kwargs={"app": app, "replace_existing": True},
    )
    scheduler.start()


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startup SthaliScheduler")
    print(
        """
minute hour day-of-month month day-of-week command
m      h    dom          mon   dow         command

*      *    *            *     *           curl -X GET 0.0.0.0:9000/cats/
        """
    )
    await setup_scheduler(app)
    yield
    print("Shutdown SthaliScheduler")
