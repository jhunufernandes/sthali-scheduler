from os import path

from sthali_crud import AppSpecification, SthaliCRUD

TINYDB_PATH = path.join(path.dirname(__file__), "../../tinydb.json")
SPEC = {
    "resources": [
        {
            "db": {"engine": "tinydb", "path": TINYDB_PATH},
            "name": "cats",
            "fields": [
                {
                    "name": "name",
                    "type": str,
                },
                {
                    "name": "age",
                    "type": int,
                },
            ],
        },
        {
            "db": {"engine": "tinydb", "path": TINYDB_PATH},
            "name": "dogs",
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


app = SthaliCRUD(AppSpecification(**SPEC)).app
