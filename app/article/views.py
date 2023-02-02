from flask import render_template, request, redirect, url_for
from app.models import Article, Author, Tag, db
from app.article import bp
from app.article.forms import ArticleForm
from flask_login import current_user, login_required

from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound


@bp.route("/articles/")
def list():
    articles = Article.query.all()
    return render_template("article/list.html", articles=articles)


# @bp.route('/articles/<int:article_id>/', methods=['GET'])
# def article_detail(article_id):
#     _article: Article = Article.query.filter_by(
#         id=article_id
#     ).options(
#         joinedload(Article.tags)
#     ).one_or_none()

#     if _article is None:
#         raise NotFound
#     return render_template(
#         'articles/detail.html',
#         article=_article,
#     )

@bp.route("/articles/<int:id>/")
def detail(id):
    article: Article = Article.query.filter_by(id=id).options(joinedload(Article.tags)).one_or_none()

    if article is None:
        raise NotFound
    return render_template("article/detail.html", article=article)


@bp.route("/articles/create/", methods=["GET", "POST"])
@login_required
def create(id=None):
    if not current_user.is_authenticated:
        return redirect(url_for("user.login"))
    
    if id:
        article = Article.query.filter_by(id=id).first()
        form = ArticleForm(request.form, obj=article)

    else: 
        form = ArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    

    
    if form.validate_on_submit():
        article = Article(title=form.title.data.strip(), body=form.body.data)

        if current_user.author:
            article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)

        db.session.add(article)
        db.session.commit()

        return redirect(url_for('article.detail', id=article.id))
    
    return render_template("article/form.html", form=form)


@bp.route("/articles/<int:id>/update/", methods=["GET", "POST"])
@login_required
def update(id):
    if not current_user.is_authenticated:
        return redirect(url_for("user.login"))
    
    article = Article.query.filter_by(id=id).first()
    form = ArticleForm(request.form, obj=article)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    
    if form.validate_on_submit():
        article = Article(title=form.title.data.strip(), body=form.body.data)

        if current_user.author:
            article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)

        db.session.add(article)
        db.session.commit()

        return redirect(url_for('article.detail', id=article.id))
    
    return render_template("article/form.html", form=form)



@bp.route("/articles/<int:id>/delete/", methods=["GET", "POST"])
@login_required
def delete(id):
    article = Article.query.get(id)
    if request.method == "POST":
        db.session.delete(article)
        db.session.commit()
        return redirect(url_for(".list"))
        # return render_template("deleted_successfully.html")
    return render_template("confirme_delete.html", object=article)


# @db.route("/articles/<int:id>/tag/add")
# @login_required
# def add_tag(id):
#     aritcle: Article = Article.query.get(id)
#     tags = aritcle.tags.all()
#     # form = TagForm
#     aritcle.add_tag()
