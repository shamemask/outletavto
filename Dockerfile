# Определение базового образа
FROM python:3.9-slim-buster

# Установим зависимости
RUN apt-get update -y && apt-get install -y libpq-dev nginx mc

# Настройка рабочей директории
WORKDIR /srv/www/outletavto

# Копирование зависимостей приложения
COPY requirements.txt .

# Установка зависимостей
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копирование исходных файлов приложения
COPY . .

# Запуск миграций базы данных
# RUN python manage.py migrate

# Установка переменных среды
# ENV DJANGO_SETTINGS_MODULE=myproject.settings.production

# Открытие порта
EXPOSE 8000


# Запуск сервера Django
# CMD gunicorn --bind 0.0.0.0:8000 wsgi:app