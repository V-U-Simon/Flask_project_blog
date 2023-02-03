from flask import Flask
from app.config import Config
from app import commands

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_admin import Admin



db = SQLAlchemy()
login = LoginManager()
bootstrap = Bootstrap()
migrate = Migrate()
admin = Admin(name="Article Admin Panel", template_mode="bootstrap4")


def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)
    register_commands(app)
    register_blueprints(app)

    from app import models
    
    
    from flask_admin.contrib.sqla import ModelView
    
    class CustomAdminView(ModelView):

        def create_blueprint(self, admin):
            blueprint = super().create_blueprint(admin)
            blueprint.name = f'{blueprint.name}_admin'
            return blueprint
        
        
        def get_url(self, endpoint, **kwargs):
            if not (endpoint.startswith('.') or endpoint.startswith('admin.')):
                endpoint = endpoint.replace('.', '_admin.')
            return super().get_url(endpoint, **kwargs)
    
    admin.add_view(CustomAdminView(models.Article, db.session, category='Models'))
    
    return app


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = "user.login"
    bootstrap.init_app(app)
    admin.init_app(app)


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
    
    
    # from app.admin import register_views
    # register_views()
    # from app.admin import bp as admin_bp
    # app.register_blueprint(admin_bp, url_prefix="/admin")
    # fmt: on
