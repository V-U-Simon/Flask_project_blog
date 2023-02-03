---
aliases: [ ]
tags:
created: 2023.02.03 8:19:35 вечера
modified: 2023.02.03 8:19:56 вечера
---

🚀 запуск приложения [[flask/README.md|Flask]] через терминал:

```Bash
# передача 📦 переменной окружения 
# с указанием на 📁 файл содержащий экземпляр прилжоения
export FLASK_APP=wsgi.py  

flask run            # 🚀 Запуск приложения
poetry run flask run # 🚀 Запуск приложения через poetry
```

🚀 запуск через питоновский файл

```python
# ... экземпляр `app` Flask прилоежния

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
```
