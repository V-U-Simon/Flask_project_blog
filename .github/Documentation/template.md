---
aliases: [ ]
tags:
created: 2022.12.23 3:25:40 дня
modified: 2023.01.01 2:07:10 дня
---

 во [[flask/README.md|flask]] используется шаблонизатор [[📚 Jinja2|Jinja]]

> - [[контекст]]

```python
from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

Расположение шаблонов

```Bash
/application.py
/templates
    /hello.html
```

```Bash
/application
    /__init__.py
    /templates
        /hello.html
```

```django
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
```

имеется доступ к объектам
- [`request`](https://flask-russian-docs.readthedocs.io/ru/master/api.html#flask.request "flask.request"), 
- [`session`](https://flask-russian-docs.readthedocs.io/ru/master/api.html#flask.session "flask.session") и 
- [`g`](https://flask-russian-docs.readthedocs.io/ru/master/api.html#flask.g "flask.g")
- функции [`get_flashed_messages()`](https://flask-russian-docs.readthedocs.io/ru/master/api.html#flask.get_flashed_messages "flask.get_flashed_messages")
