import os
from dotenv import load_dotenv

project_path = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(project_path, ".env"))


class ConfigPostgres:
    # example "postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@:{POSTGRES_PORT}/{POSTGRES_DB}"
    # POSTGRES_URI = "postgresql://user:password@localhost:5432/blog"
    # POSTGRES_URI = "postgresql://user:password@service_db:5432/db_name"
    POSTGRES_URI = "postgresql://user:password@localhost:5432/db_name"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or POSTGRES_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigSqlite:
    SQLITE_URI = "sqlite:///" + os.path.join(project_path, "app.db")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or SQLITE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config(ConfigPostgres):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
