---
aliases: [ ]
tags:
created: 2022.12.23 3:24:04 дня
modified: 2022.12.23 4:40:57 дня
---
[^#]:: [объект запроса `flask.Request`](https://docs-python.ru/packages/veb-frejmvork-flask-python/klass-request/ "Класс Request() модуля flask в Python.")
[^#]:: [Получение данных из запроса в приложении на Flask.](https://docs-python.ru/packages/veb-frejmvork-flask-python/dostup-razlichnym-dannym-zaprosa-flask/)


```python
from flask import request


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': do_the_login()
    else: show_the_login_form()
```


Получение доступа к параметрам url

```python
# /page?key=value
searchword = request.args.get('key', '')
```
