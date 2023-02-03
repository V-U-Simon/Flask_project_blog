---
aliases: [ ]
tags:
created: 2022.12.23 4:53:38 дня
modified: 2022.12.23 4:55:35 дня
---



```python
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
	def index(): 
		return ответ, статус, заголовки

@app.route('/')
	def index(): 
		return 'string'


@app.errorhandler(404)
def not_found(error):
    responce_obj = make_response(render_template('error.html'), 404)
    responce_obj.headers['X-Something'] = 'A value'
    return responce_obj
```
