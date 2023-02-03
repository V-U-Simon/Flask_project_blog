---
aliases: ['flask db config', 'flask database config', ]
tags:
created: 2023.01.01 6:09:17 вечера
modified: 2023.01.03 7:55:25 вечера
---
[^#]:: 🇺🇸 [flask-sqlalchemy — documentation](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)
[^#]:: 🇺🇸 [flask-sqlalchemy — Configuration Keys](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/config/#flask_sqlalchemy.config.SQLALCHEMY_DATABASE_URI)
[^#]:: [URI для подключения Postgres](https://postgrespro.ru/docs/postgresql/15/libpq-connect#LIBPQ-CONNSTRING)

Установка и настройка конфигурации [[💾 flask db|Flask]] базы данных на основе [[📚 sqlalchemy|SQLAlchemy]].

📀 Установка

```Bash
poetry add flask-sqlalchemy 
```

⚙️ [[flask/⚙️ config|конфигурирование]] настроек базы данных, применяемых к приложению (➕ [[connect to DB|подключение к базе данных]])

[^#]:: [Find the host name and port using PSQL commands](https://stackoverflow.com/questions/5598517/find-the-host-name-and-port-using-psql-commands)
```python
import os
base_dir = os.path.abspath(os.path.dirname(__file__))

DB_URI = 'sqlite:///' + os.path.join(base_dir, 'app.db')
# dialect://username:password@host:port/database
# sqlite:///project.db # SQLite, relative to Flask instance path
# postgresql://scott:tiger@localhost/project # PostgreSQL
# mysql://scott:tiger@localhost/project # MySQL / MariaDB

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False # уведомления о необходимости внесения изменений
```

🔌 инициализация

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def register_extensions(app: Flask):
	# initialize the app with the extension
    db.init_app(app)

# app = Flask(__name__)
# def register_extensions(app)


from app import models # определить структуру базы данных
```

💾 Не забываем про [[💾 flask migration|миграции]]
