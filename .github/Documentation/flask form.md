---
aliases: ['WTForm', 'flask form',  ]
tags:
created: 2023.01.01 1:37:59 дня
modified: 2023.01.15 11:40:38 утра
---
[^#]:: 🇺🇸 [WTForms](https://wtforms.readthedocs.io/en/3.0.x/index.html) — flexible forms, validation and rendering library
[^#]:: 🇺🇸 [Flask-WTF](https://flask-wtf.readthedocs.io/en/latest/) —  including WTForms, CSRF, file upload, and reCAPTCHA ⭐

[^#]:: [Идеальная форма. Обрабатываем сложные формы на Python с помощью WTForms](https://xakep.ru/2018/09/24/wtforms/)
[^#]:: [Мега-Учебник Flask, Часть 3: Веб-формы (издание 2018)](https://habr.com/ru/post/346342/)


📀 Установка

```Bash
# ℹ️  Нет необходимости регистрировать приложения
poetry add Flask-WTF # ⭐ include WTForms
# poetry add WTForms
```

Далее рассматриваем создание формы с помощью *`Flask-WTF`*.

🔒 необходимо настроить секретный ключ в [[flask/⚙️ config|⚙️ config]]

👔 настраиваем поля формы 📁 `project/app/forms.py`

```python
from flask_wtf import FlaskForm # 🎓 класс формы импортируем из Flask-WTF
# остальные элементы формы из стандартной библиотеки WTForms
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
```

view

```python
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
	    message = f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}'
        flash(message)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
```

template 📁 `templates/login.html`

```HTML
{% extends "base.html" %}

{% block content %}
    <h1>Sign In</h1>
    <form action="" method="post"  novalidate>
        {{ form.hidden_tag() }} {# !!! IMPORTANT TO ADD CSRF TOCKEN !!! #}
        <p>
            {{ form.username.label }}<br>
            {{ form.username(size=32) }}<br>
            {% for error in form.username.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>
            {{ form.password.label }}<br>
            {{ form.password(size=32) }}<br>
            {% for error in form.password.errors %}
            <span style="color: red;">[{{ error }}]</span>
            {% endfor %}
        </p>
        <p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
        <p>{{ form.submit() }}</p>
    </form>
 {% endblock %}
```
