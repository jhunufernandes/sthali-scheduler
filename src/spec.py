from os import path
from uuid import UUID

TINYDB_PATH = path.join(path.dirname(__file__), "../volume/tinydb.json")
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
                    "name": "minute",
                    "type": str,
                },
                {
                    "name": "hour",
                    "type": str,
                },
                {
                    "name": "day_of_month",
                    "type": str,
                },
                {
                    "name": "month",
                    "type": str,
                },
                {
                    "name": "day_of_week",
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
            ],
        },
    ]
}
