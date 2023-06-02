# Определение базового образа
FROM python:3.9-slim-buster

# Установка Nginx
RUN apt-get update  && apt-get install -y apt-utils && apt-get install -y nginx

# Настройка конфигурации Nginx
COPY outletauto_nginx.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/outletauto_nginx.conf /etc/nginx/sites-enabled/

# Настройка рабочей директории
WORKDIR /app

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

# Запуск сервера Django через Gunicorn через Nginx
CMD service nginx start && gunicorn --bind 0.0.0.0:8000 wsgi:app