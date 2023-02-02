from flask import Flask

from app import commands
from app import db, login_manager, migrate, csrf, admin
from app.models import User


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')

    register_extensions(app)
    register_blueprints(app)
    # register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprints(app: Flask):
    # from app.auth.views import auth
    from app.user.views import user
    # from app.author.views import author
    from app.article.views import article
    from app import admin

    app.register_blueprint(user)
    # app.register_blueprint(auth)
    # app.register_blueprint(author)
    app.register_blueprint(article)

    admin.register_views()