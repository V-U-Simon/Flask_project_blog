---
aliases: [ ]
tags:
created: 2023.01.01 10:39:28 вечера
modified: 2023.01.02 6:47:32 вечера
---

[^#]:: [Вход пользователей в систему](https://habr.com/ru/post/346346/)
```python
# ...
from flask_login import current_user, login_user, logout_user
from app.models import User

# ...

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
		# в дальнейшем запомнить пользователя
        login_user(user, remember=form.remember_me.data) 
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
```

```django
{% block app_content %}
    <h1>{{ _('Sign In') }}</h1>
    <div class="row">
        <div class="col-md-4">
            {{ wtf.quick_form(form) }}
        </div>
    </div>
    <br>
    <p>{{ _('New User?') }} <a href="{{ url_for('auth.register') }}">{{ _('Click to Register!') }}</a></p>
    <p>
        {{ _('Forgot Your Password?') }}
        <a href="{{ url_for('auth.reset_password_request') }}">{{ _('Click to Reset It') }}</a>
    </p>
{% endblock %}
```
