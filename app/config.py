import os
from dotenv import load_dotenv

project_path = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(project_path, ".env"))


class ConfigPostgres:
    POSTGRES_URI = "postgresql://:5432/flask_db"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or POSTGRES_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigSqlite:
    SQLITE_URI = "sqlite:///" + os.path.join(project_path, "app.db")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or SQLITE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config(ConfigPostgres):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
