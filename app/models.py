from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = "user_table"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    is_staff = db.Column(db.Boolean(), default=False)
    password_hash = db.Column(db.String(128))

    author = db.relationship("Author", backref="user", uselist=False)

    def __str__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @property
    def is_author(self) -> bool:
        return bool(self.author)
        


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Author(db.Model):
    __tablename__ = "author_table"
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user_table.id"), nullable=True)
    articles = db.relationship("Article", backref="author")

    def __repr__(self):
        return f"<Author: {self.user}>"


class Article(db.Model):
    __tablename__ = "article_table"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    author_id = db.Column(db.Integer, db.ForeignKey("author_table.id"), nullable=True)

    def __repr__(self):
        return f"<Article {self.title}>"
