---
aliases: [ ]
tags:
created: 2023.02.03 10:20:10 вечера
modified: 2023.02.03 10:20:52 вечера
---

# Getting started this project

By pip

1. Clone this repository
2. Navigate to the project directory
3. Create a virtual environment
4. Activate the virtual environment
5. Install the required packages
6. Open a web browser and navigate to [http://localhost:5000](http://localhost:5000/)

bashCopy code

```Bash
git clone https://github.com/[your-username]/flask-experience.git
cd flask-experience
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```
