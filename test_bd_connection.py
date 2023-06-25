import mysql.connector

try:
    # Установка параметров подключения
    connection_config = {
        'user': 'u2040455_default',
        'password': 'yfMhL7PiOB30M9WN',
        'host': '31.31.196.224',
        'port': 3306,
        'database': 'u2040455_default'
    }

    # Подключение к базе данных
    connection = mysql.connector.connect(**connection_config)

    # Проверка подключения
    if connection.is_connected():
        print('Подключение к базе данных успешно установлено.')
    else:
        print('Не удалось подключиться к базе данных.')

    # Закрытие подключения
    connection.close()

except mysql.connector.Error as error:
    print('Ошибка при подключении к базе данных:', error)
