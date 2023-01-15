from app.user import bp

from flask import flash, render_template, redirect, url_for
from flask_login import current_user, login_required, login_user, logout_user
from app.user.forms import RegistrationForm, LoginForm

from app import db
from app.models import User


@bp.route("/registration", methods=["GET", "POST"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for(".profile", id=current_user.id))

    form = RegistrationForm()

    if form.validate_on_submit():
        user_by_username = User.query.filter_by(username=form.username.data)
        user_by_email = User.query.filter_by(email=form.email.data)
        user = user_by_username.first() or user_by_email.first()

        if user:
            return redirect(url_for(".registration"))

        u = User(username=form.username.data, email=form.email.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
        login_user(u)

        return redirect(url_for(".profile", id=current_user.id))

    return render_template("user/registration.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for(".list"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        # авторизовать пользователя (в дальнейшем запомнить)
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for(".profile", id=current_user.id))
    return render_template("user/login.html", form=form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for(".login"))


@bp.route("")
def list():
    users = User.query.all()
    print(users)
    return render_template("user/list.html", users=users)


@bp.route("/<int:id>")
@login_required
def profile(id: int):
    user = User.query.filter_by(id=id).first()
    return render_template("user/profile.html", user=user)


@bp.route("/<int:id>/update", methods=["GET", "POST"])
def update(id: int):
    return render_template("user/update.html")


@bp.route("/<int:id>/delete", methods=["GET", "POST"])
def delete(id: int):
    return render_template("user/delete.html")


@bp.route("/<int:id>/confirme_delete", methods=["GET", "POST"])
def confirme_delete(id: int):
    return render_template("user/confirme_delete.html")

    # if request.method == "POST":
    #     username = request.form.get("username")
    #     password = request.form.get("password")

    #     user = User.query.filter_by(username=username).first()

    #     if not user or not user.check_password(password):
    #         flash("Check your username or password")
    #         return redirect(url_for(".login"))

    #     login_user(user)
    #     return redirect(url_for(".detail", pk=user.id))
