---
aliases: [ ]
tags:
created: 2023.01.01 7:21:49 вечера
modified: 2023.02.03 8:50:20 вечера
---
[^#]:: 🇺🇸 [Flask-Login](https://flask-login.readthedocs.io/en/latest/index.html)
[^#]:: 🇷🇺 digitalocean [Добавление аутентификации в ваше приложение с помощью Flask-Login](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login-ru)
[^#]:: 🇷🇺 [Мега-Учебник Flask, Часть 5: Пользовательские логины (издание 2018)](https://habr.com/ru/post/346346/)

Особенности реализации создания пользователя и его авторизации

Установка приложения

```Bash
poetry add flask-login;
poetry add flask-wtf;
poetry add email_validator;
```

Инициализация приложения в 📁 `app/__init__.py`

```python
# ...
from flask_login import LoginManager

app = Flask(__name__)
# ...
login = LoginManager(app)
login.login_view = 'login' # перенаправление неавторизованного пользователя
# 'login' - endpoint (функция для авторизации, передается в url_for)
# /login?Next=/index
# ...
```

- Добавление обязательных свойств в [[🧩👤 модель пользователя|модель пользователя]]
- Добавление проверки и установки [[🧩👤 hash password|хеша паролей]].
- Добавление пользовательского [[🧩👤 загрузчика|загрузчика]] — указывает на идентификатор пользователя
- определение view(`app/routes.py`)
	- [[🧩👤 login|вход пользователя]] (индентификации), выхода
	- [[🧩👤 logout|выход пользователя]]
	- [[🧩👤 регистрация пользователя|регистрация пользователя]]
	- [[🧩👤 ограничение доступа|ограничение доступа]]
	- [[🧩👤 показать|показать]] авторизованного пользователя
