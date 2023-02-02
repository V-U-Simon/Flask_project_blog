from flask import Flask
from app.config import Config
from app import commands

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
login = LoginManager()
bootstrap = Bootstrap()
migrate = Migrate()


def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)
    register_commands(app)
    register_blueprints(app)

    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'user.login'
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
