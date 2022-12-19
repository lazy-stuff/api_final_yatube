# API Yatube
 

##### API для Yatube - социальной сети для блогеров.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
$ git clone https://github.com/lazy-stuff/api_final_yatube
$ cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:

```
$ python3 -m venv venv
$ source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
$ python3 -m pip install --upgrade pip
$ pip install -r requirements.txt
```

Выполнить миграции:

```
$ python3 manage.py migrate
```

Запустить проект:

```
$ python3 manage.py runserver
```
#### Технологии
  
* [Python](https://www.python.org)

* [Django REST framework](https://www.django-rest-framework.org)

#### Автор

**Настя Лунегова** - *GitHub* - *[lazy-stuff](https://github.com/lazy-stuff)*

#### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
