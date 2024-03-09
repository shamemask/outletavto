# outletavto
outletavto.ru


### ТЕХНОЛОГИИ


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

# virtual env

```cmd
python -m venv venv
```

✅ linux
```cmd
source venv/bin/activate
```

✅ windows
```cmd
venv\Scripts\activate
```

# Установка зависимостей в виртуальной среде

✅ linux
```
pip install -r requirements.txt
```

✅ windows
```
pip install -r requirements_win.txt
```

✅ Выполнить миграцию

```
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations abcp_parser
python manage.py migrate abcp_parser
```

✅ Запустить сервер

```
python manage.py runserver
```

✅ Проверить доступность проекта на

```
http://localhost:8000/
```

# Для настройки парсера

✅ Скачать geeckodriver со страницы https://github.com/mozilla/geckodriver/releases/

## Для Windows
✅ скопировать файл geckodriver.exe в директорию C:\Windows\System32


