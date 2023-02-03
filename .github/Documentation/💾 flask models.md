---
aliases: [ ]
tags:
created: 2023.01.01 6:11:30 вечера
modified: 2023.01.01 6:11:43 вечера
---
[^#]::  [WWW SQL Designer](http://ondras.zarovi.cz/sql/demo) - инструмент для графического отображения БД

Создание структуры (схемы) базы данных

```python
from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
```

Альтернативное создание схемы через чистый sql

```SQL
-- 📁 flaskr/schema.sql
drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);
```

```Bash
sqlite3 /tmp/flaskr.db < schema.sql
```
