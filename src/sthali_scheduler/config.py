from contextlib import asynccontextmanager

from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI


def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)


async def get_schedules(app: FastAPI) -> list:
    print("Get schedules")
    return [
        {
            "minute": schedule["minute"],
            "hour": schedule["hour"],
            "day": schedule["day_of_month"],
            "month": schedule["month"],
            "day_of_week": schedule["day_of_week"],
            "args": schedule
        }
        for schedule in await app.extra["db"]["schedules"].read_all()
    ]


async def setup_scheduler(app: FastAPI) -> None:
    print("Setup Scheduler")
    scheduler = BackgroundScheduler()
    for schecule in await get_schedules(app):
        scheduler.add_job(myfunc, "cron", **schecule)
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
