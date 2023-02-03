---
aliases: [ ]
tags:
created: 2023.01.01 10:40:06 вечера
modified: 2023.01.01 11:20:46 вечера
---

```python
@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))
```

отображение входа/выхода из аккаунта в `template`

```django
{% if current_user.is_anonymous %}
	<a href="{{ url_for('login') }}">Login</a>
{% else %}
	<a href="{{ url_for('logout') }}">Logout</a>
{% endif %}
```
