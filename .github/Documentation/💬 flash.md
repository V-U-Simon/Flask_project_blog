---
aliases: ['flask flash', 'flask messages',  ]
tags:
created: 2023.01.01 2:08:15 дня
modified: 2023.01.01 2:14:19 дня
---

Всплывающие сообщения основанные на [[🔀 сессии|сессиях]], отображающиеся один раз, затем удаляющиеся

Есть смысл в добавлении в базовый шаблон.

```django
{% with messages = get_flashed_messages() %}
	{% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
	{% endif %}
{% endwith %}
```

`with`, чтобы назначить результат вызова `get_flashed_messages()` переменной `messages`

```python
from flask import render_template, flash, redirect

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
	    message = f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}'
        flash(message)
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
```
