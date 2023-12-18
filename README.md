# outletavto
outletavto.ru


### ТЕХНОЛОГИИ

HR Prakticum Career разработан с использованием следующих технологий:

- [Python] (v.3.11) - целевой язык программирования backend
- [Django] (v.4.2) - высокоуровневый веб-фреймворк
- [PostgreSQL] (v.13.10) - объектно-реляционная база данных
- [Gunicorn] (v.21.2) - Python WSGI HTTP-сервер для UNIX
- [Nginx] - HTTP-сервер и обратный прокси-сервер
- [Docker] (v.24.0) - инструмент для автоматизирования процессов разработки, доставки и запуска приложений в контейнерах

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)


___


### РАЗВЕРТКА

✅ Создать корневую папку с проектом (предлагается "hakaton") и перейти в неё

```
mkdir hakaton
cd hakaton
```

✅ Клонировать outletavto

```
git clone https://github.com/shamemask/outletavto.git
```

✅ Перейти в папку outletavto

```
cd outletavto
```

✅ Загрузить сабмодули

```
git submodule update --init -f
```

✅ Развернуть через docker

```
docker-compose up --build -d
```
## ЛИБО Развернуть локально

✅ Установить poetry ([Установка Poetry под Windows](https://teletype.in/@alenkimov/poetry))

```cmd
curl -sSL https://install.python-poetry.org | python -
```

✅ Установить зависимости

```
poetry install --no-root --no-interaction --no-ansi
```

✅ Войти в виртуальную среду
```
poetry shell
```

✅ Установить конфликтную билиотеку
```
pip install psycopg2 
```

✅ Выполнить миграцию

```
python manage.py makemigrations
python manage.py migrate
```

✅ Запустить сервер

```
python manage.py runserver
```

✅ Проверить доступность проекта на

```
http://localhost:8000/
```

