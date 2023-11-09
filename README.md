<p align="center">
    <a href="https://jhunufernandes.github.io/sthali-scheduler/docs/images/scheduler.svg">
        <img src="https://jhunufernandes.github.io/sthali-scheduler/docs/images/scheduler.svg" alt="SthaliScheduler" height="35%">
    </a>
    <em>A FastAPI package for schedule tasks</em>
</p>
<p align="center">
    <a href="https://pypi.org/project/sthali-scheduler/" target="_blank">
        <img src="https://img.shields.io/pypi/v/sthali-scheduler?label=Python%20Version&logo=python&color=%23ca5b32&logoColor=white" alt="">
    </a>
    <a href="https://github.com/jhunufernandes/sthali-scheduler/blob/main/docs/LICENSE" target="_blank">
        <img src="https://img.shields.io/github/license/jhunufernandes/sthali-scheduler?label=License&logo=opensourceinitiative&color=%23ca5b32&logoColor=white" alt="">
    </a>
</p>
<p align="center">
    <a href="https://github.com/jhunufernandes/sthali-scheduler/actions/workflows/test-package.yml" target="_blank">
        <img src="https://github.com/jhunufernandes/sthali-scheduler/actions/workflows/test-package.yml/badge.svg" alt="">
    </a>
    <a href="https://github.com/jhunufernandes/sthali-scheduler/actions/workflows/build-upload-pypi.yml" target="_blank">
        <img src="https://github.com/jhunufernandes/sthali-scheduler/actions/workflows/build-upload-pypi.yml/badge.svg" alt="">
    </a>
    <a href="https://github.com/jhunufernandes/sthali-scheduler/actions/workflows/build-upload-dockerhub.yml" target="_blank">
        <img src="https://github.com/jhunufernandes/sthali-scheduler/actions/workflows/build-upload-dockerhub.yml/badge.svg" alt="">
    </a>
    <a href="https://github.com/jhunufernandes/sthali-scheduler/actions/workflows/build-upload-ghcr.yml" target="_blank">
        <img src="https://github.com/jhunufernandes/sthali-scheduler/actions/workflows/build-upload-ghcr.yml/badge.svg" alt="">
    </a>
</p>

**Docs**: [https://jhunufernandes.github.io/sthali-scheduler/](https://jhunufernandes.github.io/sthali-scheduler/)

**PyPI**: [https://pypi.org/project/sthali-scheduler/](https://pypi.org/project/sthali-scheduler/)

**Source Code**: [https://github.com/jhunufernandes/sthali-scheduler/](https://github.com/jhunufernandes/sthali-scheduler/)

**Sthali Board**: [https://github.com/users/jhunufernandes/projects/4/](https://github.com/users/jhunufernandes/projects/4/)



---



## Requirements

Python >= 3.11
* [SthaliCRUD](https://github.com/jhunufernandes/sthali-crud/)
* [APScheduler](https://apscheduler.readthedocs.io/)
* [HTTPX](https://www.python-httpx.org/)
* [uvicorn](https://www.uvicorn.org/)



## Test

You can test this package alone by cloning the repo

```console
$ git clone https://github.com/jhunufernandes/sthali-scheduler/
...
config your env
...
(.venv)$ export ENV=DOCKER
(.venv)$ ./run.sh
```

or pulling the container.

```console
$ docker pull jhunufernandes/sthali-scheduler
$ export ENV=DOCKER
$ ./run.sh
```

#### Automatic API docs

Now go to [http://127.0.0.1:9000/docs](http://127.0.0.1:9000/docs). You will see the automatic interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)).

#### Alternative API docs

And now, go to [http://127.0.0.1:9000/redoc](http://127.0.0.1:9000/redoc). You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>).



## Usage

```console
$ pip install sthali-scheduler
```



## License

This project is licensed under the terms of the [MIT license](docs/LICENSE).
