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

# COPY static /srv/www/outletavto/static


# Установка переменных среды
# ENV DJANGO_SETTINGS_MODULE=myproject.settings.production

# Открытие порта
EXPOSE 8000

# Очистка кэша pip
RUN pip cache purge

# Сборка статических файлов Django
RUN python manage.py collectstatic --noinput

# Запуск Gunicorn
CMD gunicorn myproject.wsgi:application --bind 0.0.0.0:8000