---
aliases: ['flask static', ]
tags:
created: 2022.12.23 3:22:18 дня
modified: 2022.12.26 11:31:02 утра
---

```Bash
# 📁 static/style.css
```

```python
from flask import url_for

url_for('static', filename='css/styles.css')
```

```django
# static/css/styles.css
<link type="text/css" href="{{ url_for('static', filename='css/styles.css') }}" rel="stylesheet">       # static/css/styles.css
<link type="text/css" href="{{ url_for('.static', filename='css/styles.css') }}" rel="stylesheet">      # admin/static/css/styles.css
```
