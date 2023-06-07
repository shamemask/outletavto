# Определение базового образа
FROM python:3.9-slim-buster

# Установим зависимости
RUN apt-get update -y && apt-get install -y libpq-dev nginx mc

# Настройка рабочей директории
WORKDIR /srv/www/outletavto

# Копирование зависимостей приложения
COPY requirements.txt .

# Установка зависимостей
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Копирование исходных файлов приложения
COPY . .

# Запуск миграций базы данных
# RUN python manage.py migrate

# Копирование статических файлов
COPY static /srv/www/outletavto/static

COPY static/outletauto/index.html /srv/www/outletavto/

# CMD python manage.py collectstatic

# Открытие порта
EXPOSE 8000

# Запуск Gunicorn
# CMD gunicorn outletavto.wsgi:application --bind 0.0.0.0:8000
