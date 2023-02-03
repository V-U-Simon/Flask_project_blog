---
aliases: [ ]
tags:
created: 2023.01.03 7:53:40 вечера
modified: 2023.01.03 7:53:41 вечера
---

Не эффективный вариант подключения к БД

```python
def connect_db():
    """Соединяет с указанной базой данных."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

```

Эффективный подход к подключению БД использую [[контекст|контекст приложения]]

```python
def get_db():
    """Если ещё нет соединения с базой данных, открыть новое - для
    текущего контекста приложения
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


```

Разрыва соединения `teardown_appcontext()` выполняется каждый раз, когда происходит разрыв контекста приложения.

В сущности, контекст приложения уже создан до того, как пришёл запрос, и он уничтожается (разрывается) когда запрос заканчивается.

Разрыв может произойти по двум причинам:
- или всё прошло хорошо (параметр ошибки в этом случае будет None),
- или произошло исключение, и в этом случае функции разрыва будет передана ошибка.

```python


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
        
```
