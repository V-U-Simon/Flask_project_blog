---
aliases: ['flask config',  ]
tags:
created: 2022.12.23 7:11:12 вечера
modified: 2023.02.03 8:18:31 вечера
---

Конфигурация [[flask/README.md|Flask]] проекта:

⚙️ Определяем конфигурационные переменные с приоритетом назначения из 📦 [[environment variable|переменных окружения]]

```bash
SECRET_KEY # для ширования сессий
```

```python
# 📁 app/config.py
from dotenv import dotenv_values
config = dotenv_values(".env") 


class AnotherConfig(Config):
	USERNAME = config['USERNAME']
	PASSWORD = config['PASSWORD']


config_dict = {
	USERNAME='user',
    PASSWORD='pass',
}
```

Применение конфига

```python
# 📁 app/__init__.py
from flask import Flask
from app.cofing import Config, config_dict

app = Flask(__name__)
app.config.from_object(Config)              # 🎓 из класса
app.config.from_envvar('.env', silent=True) # 📁 из файла
app.config.update(config_dict)              # 📦 из словаря
```
