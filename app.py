from flask import Flask, redirect, url_for
from user.views import user
from article.views import article


def create_app():
    app = Flask(__name__)
    register_blueprints(app)

    @app.route("/")
    def main_page():
        return redirect(url_for("user.list"))

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(article, url_prefix="/article")
