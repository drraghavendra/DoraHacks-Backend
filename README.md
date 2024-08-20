# ad manager

[![made-with-python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)

[![made-with-django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)](https://www.djangoproject.com/start/)

[![made-with-dokcer](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)


## Run Locally

Set up virtual environment

```zsh
python3 -m venv venv
```

Activate virtual environment

```zsh
source venv/bin/activate
```

Install dependencies

```zsh
pip3 install -r requirements.txt
```

Run django

```zsh
python3 manage.py runserver
```

## Docker Setup

Build Image

```zsh
docker-compose build
```

Run Container

```zsh
docker-compose up
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
