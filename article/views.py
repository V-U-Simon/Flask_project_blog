from flask import Blueprint, render_template

article = Blueprint(
    "article", __name__, template_folder="templates", static_folder="static"
)

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


@article.route("")
def list():
    return render_template("article/list.html", articles=ARTICLES)


@article.route("/by_user/<int:user_pk>")
def list_filter_by_user(user_pk):
    return render_template("article/list.html", articles=ARTICLES)


@article.route("/create", methods=["GET", "POST"])
def create():
    return render_template("article/create.html")


@article.route("/<int:pk>")
def detail(pk: int):
    return render_template("article/detail.html", article=ARTICLES[pk])


@article.route("/<int:pk>/update", methods=["GET", "POST"])
def update(pk: int):
    return render_template("article/update.html")


@article.route("/<int:pk>/delete", methods=["GET", "POST"])
def delete(pk: int):
    return render_template("article/delete.html")


@article.route("/<int:pk>/confirme_delete", methods=["GET", "POST"])
def confirme_delete(pk: int):
    return render_template("article/confirme_delete.html")
