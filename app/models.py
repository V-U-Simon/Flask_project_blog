from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(db.Model, UserMixin):
    __tablename__ = "user_table"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_staff = db.Column(db.Boolean(), default=False)
    is_deleted = db.Column(db.Boolean(), default=False)

    author = db.relationship("Author", backref="user", uselist=False)

    def __str__(self):
        return f"<User {self.username}>"

    def set_password(self, password) -> "User":
        self.password_hash = generate_password_hash(password)
        db.session.add(self)
        return self

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    @property
    def active(cls) -> db.Query:
        "Like Django object manager return a Query with a filter: User.query"
        original_query = db.session.query(cls)
        return original_query.filter(cls.is_deleted == False)

    @classmethod
    @property
    def deleted(cls) -> db.Query:
        "Like Django object manager return a Query with a filter: User.deleted"
        original_query = db.session.query(cls)
        return original_query.filter(cls.is_deleted == True)

    def delete(self):
        "Should be priority method for deletion of users"
        if not self.is_deleted:
            self.is_deleted = True
            db.session.add(self)
            return self

    def recover(self):
        "Opposite method of delete for recovery of users"
        if self.is_deleted:
            self.is_deleted = False
            db.session.add(self)
            return self

    @property
    def is_author(self) -> bool:
        return bool(self.author)

    def set_as_author(self) -> None:
        if not self.is_author:
            self.author = Author()
            db.session.add(self)
            return self

    def unset_as_author(self) -> None:
        if self.is_author:
            # necessary commit this change for correct applying check throw is_author
            db.session.delete(self.author)
            return self


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Author(db.Model):
    __tablename__ = "author_table"
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user_table.id"), nullable=True)
    articles = db.relationship("Article", backref="author", lazy="dynamic")

    def __repr__(self):
        return f"<Author: {self.user}>"

    def has_articles(self) -> bool:
        return bool(self.articles.count() > 0)

    def add_article(self, article):
        if not article in self.articles:
            self.articles.append(article)
            db.session.add(self)
            return self

    def remove_article(self, article: "Article") -> None:
        if article in self.articles:
            article = self.articles.filter_by(id=1).first()
            self.articles.remove(article)
            db.session.add(self)
            article.delete()
            return self
        # todo add exception then article not in self.articles


association_article_tag = db.Table(
    "followers",
    db.Column("tags", db.Integer, db.ForeignKey("article_table.id")),
    db.Column("articles", db.Integer, db.ForeignKey("tag_table.id")),
)


class Article(db.Model):
    __tablename__ = "article_table"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_deleted = db.Column(db.Boolean, default=False)

    author_id = db.Column(db.Integer, db.ForeignKey("author_table.id"), nullable=True)
    tags = db.relationship(
        "Tag",
        secondary=association_article_tag,
        backref=db.backref(
            "articles",
            # lazy="dynamic",
        ),
        # lazy="dynamic",
    )

    @classmethod
    @property
    def published(cls) -> db.Query:
        original_query = db.session.query(cls)
        return original_query.filter(cls.is_deleted == False)

    @classmethod
    @property
    def arhive(cls) -> db.Query:
        original_query = db.session.query(cls)
        return original_query.filter(cls.is_deleted == True)

    def __repr__(self):
        return f"<Article {self.title}>"

    def delete(self):
        if self.is_deleted != True:
            self.is_deleted = True
            db.session.add(self)
            return self

    def recover(self):
        if self.is_deleted == True:
            self.is_deleted = False
            db.session.add(self)
            return self

    def add_tag(self, tag):
        self.tags.append(tag)
        db.session.add(self)
        return self

    def remove_tag(self, tag):
        self.tags.remove(tag)
        db.session.delete(self)
        return self

    def tag_exists(self):
        return self.tags.count() != 0


class Tag(db.Model):
    __tablename__ = "tag_table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
