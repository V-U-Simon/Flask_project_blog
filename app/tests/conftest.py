import pytest

from app import create_app, db as db_, login
from app.config import TestConfig
from app.models import User, Author, Article
from flask_login import current_user, login_required, login_user, logout_user

# 🍎
@pytest.fixture(scope="session")
def app():
    app = create_app(TestConfig)
    # Creates a flask app context
    with app.app_context():
        yield app


# 💾
@pytest.fixture(scope="function")
def db(app):
    # extensions pattern explained in here https://stackoverflow.com/a/42910185/5819113
    db = db_
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()
    # db.get_engine(app_context).dispose() # https://stackoverflow.com/a/18365654/5819113


# 👤
@pytest.fixture()
def users(db) -> list[User]:
    users: list[User,] = [
        User(username="user_1", email="user_1@example.com").set_password("passwd"),
        User(username="user_2", email="user_2@example.com").set_password("passwd").set_as_author(),
        User(username="user_3", email="user_3@example.com", is_staff=True).set_password("passwd"),
        User(username="user_4", email="user_4@example.com", is_staff=True).set_password("passwd").set_as_author(),
    ]

    print(users)
    map(lambda user: db.session.add(user), users)
    db.session.commit()
    yield users


@pytest.fixture()
def auth_users(users) -> list[User]:
    users = map(lambda user: login_user(user), users)
    return users


@pytest.fixture()
def users_query(users_list) -> db_.Query:
    return User.query


@pytest.fixture()
def set_user_as_auth():
    yield login_user


@pytest.fixture()
def set_user_as_logut():
    yield logout_user


@pytest.fixture()
def articles(db, users) -> db_.Query:
    # user_author = User.query.filter(User.author.exists()).first()
    user_author = list(filter(lambda user: user.is_author, users))[0]

    articles = [
        Article(
            title=f"My title number {i}",
            body="Some text will be here for article number {i}",
            author=user_author.author,
        )
        for i in range(1, 5)
    ]

    
    map(lambda article: db.session.add(article), articles)
    db.session.commit()
    yield articles


# Tags
