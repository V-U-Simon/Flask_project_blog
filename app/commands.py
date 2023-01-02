import click
from werkzeug.security import generate_password_hash


@click.command("init-db")
def init_db():
    from app import db

    # import models for creating tables
    from app.models import User
    from wsgi import app

    db.create_all()


@click.command("create-init-user")
def create_init_user():
    from app.models import User
    from app import db
    from wsgi import app

    with app.app_context():
        u = User(
            username="susan",
            email="name@example.com",
        )
        u.set_password('cat')
        db.session.add(u)
        db.session.commit()
