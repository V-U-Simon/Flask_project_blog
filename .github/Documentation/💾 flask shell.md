---
aliases: [ ]
tags:
created: 2023.01.01 6:14:24 вечера
modified: 2023.01.03 7:51:38 вечера
---

Определение контекста для интерактивного режима [[💾 flask db|flask]] `shell` — `shell context`

Избавляет от необходимости постоянно импортировать модули при запуске через `shell`.

```Bash
flask shell
# from app import db
# from app.models import User, Post
```

Добавление функции которая будет автоматически импортирует модули в `flask shell`.

```python
# 📁 project/microblog.py
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
```
