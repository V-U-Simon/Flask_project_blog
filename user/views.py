from flask import Blueprint, render_template

user = Blueprint("user", __name__, template_folder="templates", static_folder="static")


USERS = {1: "Alice", 2: "Jon", 3: "Mike"}


@user.route("")
def list():
    return render_template("user/list.html", users=USERS)


@user.route("/create", methods=["GET", "POST"])
def create():
    return render_template("user/create.html")


@user.route("/<int:pk>")
def detail(pk: int):

    return render_template("user/detail.html", user=USERS[pk])


@user.route("/<int:pk>/update", methods=["GET", "POST"])
def update(pk: int):
    return render_template("user/update.html")


@user.route("/<int:pk>/delete", methods=["GET", "POST"])
def delete(pk: int):
    return render_template("user/delete.html")


@user.route("/<int:pk>/confirme_delete", methods=["GET", "POST"])
def confirme_delete(pk: int):
    return render_template("user/confirme_delete.html")
