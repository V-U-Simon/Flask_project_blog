---
aliases: [ ]
tags:
created: 2022.12.23 9:36:37 вечера
modified: 2023.01.01 2:06:46 дня
---
[^#]:: [Представления в веб-приложении на Flask Python.](https://docs-python.ru/packages/veb-frejmvork-flask-python/predstavlenija-veb-prilozhenii-flask/)

выполнение кода до получения запроса и после его обработки

> - [[flask form]]
> - [[💾 загрузка файла]]

добавляется в контекст приложения (`g' object`)

```python
@app.before_request
def process_before_request():
	g.start_time = time


@app.after_request
@def process_after_request(response) :
	if hasattr(g, "start_time"):
	response.headers["process-time"] = time() - g.start_time
	
	return response
```
