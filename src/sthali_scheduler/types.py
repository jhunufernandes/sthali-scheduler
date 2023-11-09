from uuid import UUID

from pydantic.dataclasses import dataclass


@dataclass
class SchedulerKwargs:
    """Scheduler kwargs"""
    minute: str
    hour: str
    day: str
    month: str
    day_of_week: str


@dataclass
class RequestKwargs:
    """Request kwargs"""
    endpoint: str
    method: str
    headers: dict
    body: dict
    query: dict


@dataclass
class APIKwargs:
    """API kwargs"""
    service: str
    request_kwargs: RequestKwargs


@dataclass
class Schedules:
    """Schedules"""

    id: str
    scheduler_kwargs: SchedulerKwargs
    api_kwargs: APIKwargs
