# Проект service_for_testing

## Описание

service_for_testing это сервис проведения тестирования по каким-либо темам.

Пользователи могут:
- проходить любой из тестовых наборов;
-	После завершения тестирования смотреть результат:
- количество правильных/неправильных ответов
- процент правильных ответов

## Технологии
- Python 3.9.13
- Django 4.1.3

## Установка проекта локально

* Склонировать репозиторий на локальную машину:
```bash
git clone https://github.com/niktere12321/service_for_testing.git
```
```bash
cd service_for_testing/
```

* Cоздать и активировать виртуальное окружение:

```bash
python -m venv env
```

```bash
source venv/Scripts/activate
```

* Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```

* Можете устоновить свои настойки в директории где находить файл settings.py назвав свой файл с настройками settings_local.py

* Выполните миграции:
```bash
cd service_for_testing/
```
```bash
python manage.py migrate
```

* Запустите сервер:
```bash
python manage.py runserver
```

---
## Техническая информация

Стек технологий: Python 3, Django.

---
## Об авторе

Терехов Никита Алексеевич
