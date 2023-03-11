# multithread_web_server
[![srv](https://github.com/Fastex007/multithread_web_server/actions/workflows/main.yml/badge.svg)](https://github.com/Fastex007/multithread_web_server/actions/workflows/main.yml)

## Описание проекта
Тестовый web-сервер.

## Доступные эндпоинты
* ```/``` - индексная страница, отдает список эндпоинтов
* ```/v1/api/``` - выполняется с задержкой 1-5 секунд, отдает текущее время в формате iso_8601 и 
количество секунд, которое выполнялся метод
* ```/health/``` - отдает количество запросов и общее время выполнения всех запросов от момента запуска сервера
* ```/reset_counter/``` - сбрасывает счетчик запросов


## Используемые зависимости
```
python-dotenv==1.0.0  # для чтения переменных окружения из файла
pytest==7.2.2  # для тестирования
```

## Запуск проекта
* #### Клонировать репозиторий
```
git clone https://github.com/Fastex007/multithread_web_server.git
```

* #### Выполнить команду
```
docker-compose up -d
```

## Переменные окружения
* ```SERVICE_ADDRESS``` - IP адрес сервиса
* ```SERVICE_PORT``` - порт сервиса
* ```THREAD_COUNT``` - количество выполняемых потоков
* ```CONTENT_TYPE="application/json"``` - тип контента
* ```ENCODING=utf_8``` - кодировка


## Автор
#### Pronkin Oleg
```
https://github.com/Fastex007
```
