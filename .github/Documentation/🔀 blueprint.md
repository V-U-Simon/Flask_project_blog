---
aliases: [ ]
tags:
created: 2022.12.24 6:10:13 вечера
modified: 2023.02.03 10:05:56 вечера
---
[^#]:: ℹ️ [Blueprints](https://explore-flask.readthedocs.io/en/latest/blueprints.html)
[^#]:: ℹ️ [Modular Applications with Blueprints](https://flask.palletsprojects.com/en/latest/blueprints/)
[^#]:: [Use a Flask Blueprint to Architect Your Applications](https://realpython.com/flask-blueprint/) ⭐

`blueprint`'ы — нужны для расширения (разделения) [[flask/README.md|Flask]] приложения с помощью дополнительных "модулей".

> Blueprint is not actually an application. When you register the Flask Blueprint in an application, you extend the application with its contents.

🆕 Инициализация в дополнительном приложении

```python
# 📁 app/article/__init__.py
from flask import Blueprint

bp = Blueprint('article', __name__)

from app.article import views 
```

	Дополнительные аргументы для Blueprint()
	# static_folder    the folder where the Blueprint’s static files can be found
	# template_folder  the folder containing the Blueprint’s templates
	# static_url_path  the URL to serve static files from
	# url_prefix       the path to prepend to all of the Blueprint’s URLs
	# url_defaults     a dictionary of default values that this Blueprint’s views will receive
	# subdomain        the subdomain that this Blueprint’s routes will match on by default
	
👮 Регистрация в основном приложении

```python
# 📁 app/__init__.py
extension = HelloExtension() # инициализируем экземпляр расширения

def create_app():
    app = Flask(__name__)    # создание flask приложения
	register_extensions(app) # 👮 регистрируем расширения
    return app


def register_blueprints(app: Flask)
	# fmt: off
	# 👮 регистрация blueprint модуля
    from app.article.views import bp as article_bp
    app.register_blueprint(article_bp, url_prefix="/article") 
    # fmt: on
```

	Дополнительные аргументы для app.register_blueprint()
	subdomain    is a subdomain that Blueprint routes will match
	url_prefix   is an optional prefix for all the Blueprint’s routes
	url_defaults is a dictionary with default values for view arguments

🐍 Использование в работе

```python
from app.article import bp
from app.models import Article, db
from flask import render_template, request


@bp.route("/articles/")
def list(request):
    articles = Article.query.all()
    return render_template("article/list.html", articles=articles)
```

> Обладает почти теми же методами для [[🔀 routing|маршрутизации]] что и обычное приложение.
