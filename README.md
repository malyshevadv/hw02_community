# Бекенд для социальной сети блогеров (backend_community_homework, часть yatube_project)

[![CI](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw02_community/actions/workflows/python-app.yml)

### Описание
Бекенд для социальной сети блогеров.

Создано и зарегистрировано приложение Posts.

Подключена база данных.

Десять последних записей выводятся на главную страницу.

В админ-зоне доступно управление объектами модели Post: можно публиковать новые записи или редактировать/удалять существующие.

Пользователь может перейти на страницу любого сообщества, где отображаются десять последних публикаций из этой группы.

### Технологии
- Python 3.7
- Django 2.2.19
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
```
### Авторы
Дарья М.
