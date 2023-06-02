# Установка базового образа
FROM python:3.9

# Копирование кода приложения
WORKDIR /usr/src/app
COPY . .

# Установка пакетов
RUN apt-get update && \
    apt-get install -y nginx supervisor && \
    pip install --no-cache-dir -r requirements.txt

# Копирование файлов конфигурации Nginx и Gunicorn
COPY infrastructure/nginx.conf /etc/nginx/sites-available/
COPY infrastructure/gunicorn.conf /etc/supervisor/conf.d/

# Настройка Nginx
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled/ && \
    rm /etc/nginx/sites-enabled/default

# Установка зависимостей Python, создание таблиц базы данных, сборка статической версии файлов и запуск сервера Gunicorn
RUN python manage.py migrate --noinput && \
    python manage.py collectstatic --noinput && \
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell && \
    chmod +x /usr/src/app/run.sh

# Запуск Nginx и сервера Gunicorn
CMD ["/usr/bin/supervisord", "-n"]