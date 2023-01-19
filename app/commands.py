import click


@click.command("create-initial-data")
def create_initial_data():
    from app.models import User, Author, Article
    from app import db
    from wsgi import app

    with app.app_context():

        User.query.delete()
        Author.query.delete()
        Article.query.delete()

        user = User(username="user_1", email="name1@example.com")
        user.set_password("pass")
        db.session.add(user)

        user_admin = User(username="admin_1", email="name2@example.com", is_staff=True)
        user_admin.set_password("pass")
        db.session.add(user_admin)

        user_author = User(
            username="author_1", email="name3@example.com", author=Author()
        )
        user_author.set_password("pass")
        db.session.add(user_author)

        for i in range(4):
            article = Article(title=f"My title {i}", body="Some text will be here")
            article.author = user_author.author
            db.session.add(article)
        db.session.commit()
