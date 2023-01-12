from flask import flash, render_template, redirect, url_for, request
from flask_login import current_user, login_required, login_user, logout_user
from app.models import User
from app.user import bp


@bp.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for(".list"))
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            flash("Check your username or password")
            return redirect(url_for(".login"))

        login_user(user)
        return redirect(url_for(".detail", pk=user.id))

    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user is None or not user.check_password(form.password.data):
    #         flash('Invalid username or password')
    #         return redirect(url_for('login'))
    # 	# авторизовать пользователя (в дальнейшем запомнить)
    #     login_user(user, remember=form.remember_me.data)
    #     return redirect(url_for('index'))
    return render_template("user/login.html")


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


@bp.route("/create", methods=["GET", "POST"])
def create():
    return render_template("user/create.html")


@bp.route("/<int:pk>")
@login_required
def detail(pk: int):
    user = User.query.filter_by(id=pk).first()
    return render_template("user/detail.html", user=user)


@bp.route("/<int:pk>/update", methods=["GET", "POST"])
def update(pk: int):
    return render_template("user/update.html")


@bp.route("/<int:pk>/delete", methods=["GET", "POST"])
def delete(pk: int):
    return render_template("user/delete.html")


@bp.route("/<int:pk>/confirme_delete", methods=["GET", "POST"])
def confirme_delete(pk: int):
    return render_template("user/confirme_delete.html")
