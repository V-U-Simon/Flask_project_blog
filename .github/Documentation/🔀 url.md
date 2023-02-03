---
aliases: [ ]
tags:
created: 2023.02.03 9:38:11 вечера
modified: 2023.02.03 9:38:13 вечера
---

url_for()


```python
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
	def index(): pass

@app.route('/login')
	def login(): pass

@app.route('/user/<username>')
	def profile(username): pass

with app.test_request_context():
	print url_for('index') # /
	print url_for('.index') # текущая функция в blueprint (подтянет имя автоматически)
	print url_for('admin.index') # текущая функция в blueprint admin
	print url_for('login') # /login
	print url_for('login', next='/') # /login?next=/
	print url_for('profile', username='John Doe') # /user/John%20Doe
```

Перенаправление

```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```



```django
<link type="text/css" href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet">       # static/css/styles.css
<link type="text/css" href="{{ url_for('.static', filename='css/styles.css') }}" rel="stylesheet">      # admin/static/css/styles.css
<link type="text/css" href="{{ url_for('admin.static' }}" rel="stylesheet"> # admin
```


```python
from flask import url_for

with user.test_request_context():
	print url_for('admin.admin_list') # получить url
	print url_for('.admin_list')      # получить url (same line)
```

```django
<link type="text/css" href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet">       # static/css/styles.css
<link type="text/css" href="{{ url_for('.static', filename='css/styles.css') }}" rel="stylesheet">      # admin/static/css/styles.css
<link type="text/css" href="{{ url_for('admin.static', filename='css/styles.css') }}" rel="stylesheet"> # admin/static/css/styles.css
```
