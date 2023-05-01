# Определение базового образа
FROM python:3.9-slim-buster

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


# Запуск сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
