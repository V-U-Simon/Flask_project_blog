from flask import Flask
from app.config import Config
from app import commands

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from app.admin.views import CustomAdminIndexView
from flask_rest_jsonapi_next import Api


db = SQLAlchemy()
login = LoginManager()
bootstrap = Bootstrap()
migrate = Migrate()
admin = Admin(index_view=CustomAdminIndexView(), name="Article Admin Panel", template_mode="bootstrap4")
api = Api()


def create_app(config_class=Config) -> Flask:
    from app import models

    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)
    register_commands(app)
    register_blueprints(app)
    register_admins(app, models)
    register_api(app, api)

    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = "user.login"
    bootstrap.init_app(app)


def register_commands(app: Flask):
    app.cli.add_command(commands.create_initial_data)


def register_blueprints(app: Flask):
    # fmt: off
    from app.main.views import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix="/user")

    from app.article import bp as article_bp
    app.register_blueprint(article_bp, url_prefix="/article")
    # fmt: on


def register_admins(app, models):
    admin.init_app(app)

    from app.admin import views

    # 🚦 any of admin views shoud be registered here by `add_vew` method
    admin.add_view(views.TagAdminView(models.Tag, db.session, category="Models"))
    admin.add_view(views.ArticleAdminView(models.Article, db.session, category="Models"))
    admin.add_view(views.UserAdminView(models.User, db.session, category="Models"))


def register_api(app, api):
    api.init_app(app)

    # fmt: off
    from app.api.tag import TagList
    from app.api.tag import TagDetail
    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag')

    from app.api.user import UserList
    from app.api.user import UserDetail
    api.route(UserList, 'user_list', '/api/users/', tag='User')
    api.route(UserDetail, 'user_detail', '/api/users/<int:id>', tag='User')

    from app.api.author import AuthorList
    from app.api.author import AuthorDetail
    api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
    api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>', tag='Author')

    from app.api.article import ArticleList
    from app.api.article import ArticleDetail
    api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
    api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>', tag='Article')
    # fmt: on
