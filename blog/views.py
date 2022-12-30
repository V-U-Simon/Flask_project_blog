from flask import Blueprint, render_template

blog = Blueprint("blog", __name__, template_folder="templates", static_folder="static")




@blog.route("")
def list():
    return render_template("blog/list.html")


@blog.route("/create", methods=["GET", "POST"])
def create():
    return render_template("blog/create.html")


@blog.route("/<int:pk>")
def detail(pk: int):
    return render_template("blog/detail.html")


@blog.route("/<int:pk>/update", methods=["GET", "POST"])
def update(pk: int):
    return render_template("blog/update.html")


@blog.route("/<int:pk>/delete", methods=["GET", "POST"])
def delete(pk: int):
    return render_template("blog/delete.html")


@blog.route("/<int:pk>/confirme_delete", methods=["GET", "POST"])
def confirme_delete(pk: int):
    return render_template("blog/confirme_delete.html")
