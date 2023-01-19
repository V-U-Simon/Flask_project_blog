from flask import render_template, request, redirect, url_for
from app.models import Article, db
from app.article import bp


@bp.route("/articles/")
def list():
    articles = Article.query.all()
    return render_template("article/list.html", articles=articles)


@bp.route("/articles/<int:id>/")
def detail(id):
    article = Article.query.get(id)
    return render_template("article/detail.html", article=article)


@bp.route("/articles/create/", methods=["GET", "POST"])
def create():
    # todo: добавить форму из WTForm | form = ArticleForm
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        author_id = request.form.get("author_id")

        article = Article(title=title, body=body, author_id=author_id)
        db.session.add(article)
        db.session.commit()

        return redirect(url_for(".list"))
    else:
        # return render_template("article/form.html", form=form)
        return render_template("article/form.html")


@bp.route("/articles/<int:id>/update/", methods=["GET", "POST"])
def update(id):
    article = Article.query.get(id)
    if request.method == "POST":
        article.title = request.form.get("title")
        article.body = request.form.get("body")
        article.author_id = request.form.get("author_id")

        db.session.commit()
        return redirect(url_for(".detail", id=id))
    else:
        return render_template("article/form.html", article=article)


@bp.route("/articles/<int:id>/delete/", methods=["GET", "POST"])
def delete(id):
    article = Article.query.get(id)
    if request.method == "POST":
        db.session.delete(article)
        db.session.commit()
        return redirect(url_for(".list"))
        # return render_template("deleted_successfully.html")
    return render_template("confirme_delete.html", object=article)
