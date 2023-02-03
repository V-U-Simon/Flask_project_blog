---
aliases: [ ]
tags:
created: 2023.01.01 7:15:40 вечера
modified: 2023.01.01 10:32:24 вечера
---
[^#]:: [Мега-Учебник Flask, Часть 5: Пользовательские логины (издание 2018)](https://habr.com/ru/post/346346/)
[^#]:: [Werkzeug](http://werkzeug.pocoo.org/)

```python
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

hash = generate_password_hash('password') # ✅ создание хеша пароля
hash # 'pbkdf2:sha256:50000$vT9fkZM8$04dfa35c6476acf7e788a1b5b3c35e217c78dc04539d295f011f01f18cd2175f'

# ❓ проверка пароля
check_password_hash(hash, 'password')       # True
check_password_hash(hash, 'wrong_password') # False
```

Добавление в `models.py`

```python
from werkzeug.security import generate_password_hash, check_password_hash
# ...

class User(db.Model):
    # ...
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
	
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
```
