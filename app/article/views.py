from flask import render_template
from app.article import bp


ARTICLES = {
    1: {
        "title": "Sample article post",
        "text": "This blog post shows a few different types of content that’s supported and styled with Bootstrap. Basic typography, lists, tables, images, code, and more are all supported as expected.",
        "author": {
            "name": "Alice",
            "id": 1,
        },
    },
}


@bp.route("")
def list():
    return render_template("article/list.html", articles=ARTICLES)


bp.route("/by_user/<int:user_pk>")
def list_filter_by_user(user_pk):
    return render_template("article/list.html", articles=ARTICLES)


@bp.route("/create", methods=["GET", "POST"])
def create():
    return render_template("article/create.html")


@bp.route("/<int:pk>")
def detail(pk: int):
    return render_template("article/detail.html", article=ARTICLES[pk])


@bp.route("/<int:pk>/update", methods=["GET", "POST"])
def update(pk: int):
    return render_template("article/update.html")


@bp.route("/<int:pk>/delete", methods=["GET", "POST"])
def delete(pk: int):
    return render_template("article/delete.html")


@bp.route("/<int:pk>/confirme_delete", methods=["GET", "POST"])
def confirme_delete(pk: int):
    return render_template("article/confirme_delete.html")
