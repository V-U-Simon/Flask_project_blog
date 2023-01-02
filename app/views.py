from app import app
from flask import redirect, url_for

@app.route("/")
def main_page():
    return redirect(url_for("app.user.list"))