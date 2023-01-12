from flask import redirect, url_for
from app.main import bp

@bp.route("/")
def main_page():
    return redirect(url_for("user.list"))