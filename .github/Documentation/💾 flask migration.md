---
aliases: ['миграции', 'flask migration',  ]
tags:
created: 2023.01.01 6:12:20 вечера
modified: 2023.01.12 4:50:38 дня
---
[^#]:: 🇺🇸 [How To Add Flask-Migrate To An Existing Project](https://blog.miguelgrinberg.com/post/how-to-add-flask-migrate-to-an-existing-project)

`flask-migrate` — [[💾 flask db|Flask]] библиотека для осуществления версионирования состояния схемы базы данных.

> - основана на [[📚 alembic]]

📀 установка

```Bash
poetry add flask-migrate # обертка над alembic (для миграций)
```

🔌 инициализация приложения в `__init__.py' (в месте где инициализируется экземпляр приложения)

```python
from flask_migrate import Migrate

migrate = Migrate

def register_extensions(app: Flask):
	migrate = Migrate(app, db)
```

Создание миграции и ее применение

```Bash
flask db init # создание репозитория с миграциями 

flask db migrate -m "user table" # ✅ создать миграцию
flask db upgrade                 # 🚀 применить миграцию к БД
flask db downgrade               # 🔻 откатить миграцию


flask db revision -m ''
```
