import os
from dotenv import load_dotenv

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, ".env"))


class Config:
    db_dir = "sqlite:///" + os.path.join(base_dir, "app.db")

    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or db_dir
    # уведомления о необходимости внесения изменений в БД
    SQLALCHEMY_TRACK_MODIFICATIONS = False
