import os
from dotenv import load_dotenv

project_path = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(project_path, ".env"))


class Postgres:
    # example "postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@:{POSTGRES_PORT}/{POSTGRES_DB}"
    # POSTGRES_URI = "postgresql://user:password@localhost:5432/blog"
    # POSTGRES_URI = "postgresql://user:password@service_db:5432/db_name"
    POSTGRES_URI = "postgresql://user:password@localhost:5432/db_name"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or POSTGRES_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Sqlite:
    SQLITE_URI = "sqlite:///" + os.path.join(project_path, "app.db")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or SQLITE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config(Postgres):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"


class TestConfig(Config):
    # Enable the TESTING flag to disable the error catching during request handling
    # so that you get better error reports when performing test requests against the application.
    TESTING = True
    DEBUG = True
    ELASTICSEARCH_URL = None
    # Bcrypt algorithm hashing rounds (reduced for testing purposes only!)
    BCRYPT_LOG_ROUNDS = 4 
    # Disable CSRF tokens in the Forms (only valid for testing purposes!)
    WTF_CSRF_ENABLED = False
    
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or f"sqlite:///{os.path.join(BASEDIR, 'instance', 'test.db')}")
