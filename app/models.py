from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime



class User(db.Model, UserMixin):
    __tablename__ = 'flask_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    is_admin = db.Column(db.Boolean(), default=False)
    password_hash = db.Column(db.String(128))
    # posts = db.relationship('Article', backref='author', lazy='dynamic')
    
    def __str__(self):
        return f'{self.username}'
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# waiting in the wings ;)
# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(140))
#     body = db.Column(db.String(256))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     language = db.Column(db.String(5))

#     def __repr__(self):
#         return f'<Article {self.title}>'