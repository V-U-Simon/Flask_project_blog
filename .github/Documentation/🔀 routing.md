---
aliases: ['flask urls',  ]
tags:
created: 2022.12.23 2:43:15 дня
modified: 2023.02.03 9:47:49 вечера
---
[^#]:: [Правила составления URL-маршрутов во Flask Python.](https://docs-python.ru/packages/veb-frejmvork-flask-python/registratsija-marshrutov-url-adresov-flask/)

Экземпляр [[flask/README.md|Flask]] приложения предоставляет методы для маршрутизации [[🔀 request|запросов]], используемые в виде декораторов:

```python
@app.route("/page")    # 
@app.errorhandler(404) # to register an error handler function
@app.before_request()  # to execute an action before every request
@app.after_request()   # to execute an action after every request
@app.template_filter() # to register a template filter at the application level
```

🔀 Стандартная маршрутизация с аргументом и без

```python
# 🚸 пути `/page/` и `/page` отличаются

@app.route("/page")
def page_without(): return "<h1>page without slash<h1>"


@app.route("/page/<string:some_id>")
def page_with_parametr(some_id): return f"<h1>{some_id}<h1>"

# <string:name> — строковое занначение
# <path:name>	— подобно поведению по умолчанию, но допускаются слэши
# <int:name>	— целочисленные значения
# <float:name>	— значения с плавающей точкой
```

🔀 🚨 Обработка ошибок запросов (изменить страницу с ошибкой)

```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

🔀 ⏰ Выполнение кода ДО или ПОСЛЕ

```python
@app.before_request
def process_before_request():
	g.start_time = time
```

```python
@app.after_request
@def process_after_request(response) :
	if hasattr(g, "start_time"):
	response.headers["process-time"] = time() - g.start_time
	return response
```

добавляется в контекст приложения (`g' object`)

🔀 📝 Фильтр для шаблонов

```python
@app.template_filter()
def reverse(s):
    return s[::-1]
```
[^#]:: https://flask.palletsprojects.com/en/1.1.x/templating/#registering-filters
