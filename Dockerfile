# Определение базового образа
FROM python:3.11-slim-buster

# Установка инструментов для выполнения команд Poetry
RUN apt-get update -y && apt-get install -y curl && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Копирование исходных файлов приложения
WORKDIR /srv/www/outletavto
COPY . .

# Установка зависимостей с помощью Poetry
RUN poetry install --no-root --no-interaction --no-ansi

# Копирование статических файлов
COPY static /srv/www/outletavto/static

# Установка прав доступа для статических файлов
RUN chmod -R 777 /srv/www/outletavto/static

# Открытие порта
EXPOSE 8000
