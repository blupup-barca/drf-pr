# LMS-система

Веб-приложение для создания и управления образовательными курсами и материалами.

## Описание

Система предоставляет:
- Создание и управление курсами
- Размещение учебных материалов
- Управление пользователями и правами доступа

## Технологии

- Python 3.10
- Django 4.2
- PostgreSQL 14
- Docker 20.10+
- GitHub Actions

## Установка

### Локальная разработка

git clone git@github.com:blupup-barcs/drf-pr.git 

cd drf-project

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cp .env.sample .env  # заполните переменные

python manage.py migrate

python manage.py runserver

### Production-развертывание

    На сервере выполните:

sudo apt update && sudo apt install docker.io

sudo systemctl enable docker

mkdir -p ~/drf-project

    Скопируйте .env в ~/drf-project/.env

    Всё готово!
    При первом деплое через CI/CD:
      Автоматически создастся systemd-сервис
      Контейнер будет запущен с автоперезапуском

CI/CD Pipeline

Автоматически при push, pull_request:

    Собирает Docker-образ
    Пушит в Docker Hub
    Разворачивает на сервере через SSH

Необходимые Secrets:

    DOCKER_HUB_USERNAME
    DOCKER_HUB_TOKEN
    SSH_KEY
    SERVER_IP