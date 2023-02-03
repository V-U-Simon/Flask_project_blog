---
aliases: [ ]
tags:
created: 2022.12.23 1:24:23 дня
modified: 2022.12.23 1:24:40 дня
---
https://werkzeug.palletsprojects.com/en/2.2.x/tutorial/#introducing-shortly


werkzeug —  реализация [[WSGI|WSGI]] используется во [[flask/README.md]]

```python
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!'.encode('utf-8')]
```

```python
from werkzeug.wrappers import Response

def application(environ, start_response):
    response = Response('Hello World!', mimetype='text/plain')
    return response(environ, start_response)


from werkzeug.wrappers import Request, Response

def application(environ, start_response):
    request = Request(environ)
    text = f"Hello {request.args.get('name', 'World')}!"
    response = Response(text, mimetype='text/plain')
    return response(environ, start_response)
```

