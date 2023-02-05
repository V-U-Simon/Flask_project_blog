import click


@click.command("create-initial-data")
def create_initial_data():
    from app.models import User, Author, Article, Tag
    from app import db
    from wsgi import app

    with app.app_context():
        db.create_all()
        
        Tag.query.delete()
        Article.query.delete()
        Author.query.delete()
        User.query.delete()

        user = User(username="user_1", email="name1@example.com")
        user.set_password("pass")
        db.session.add(user)

        user = User(username="user_2", email="namesfd1@example.com", is_deleted=True)
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
        
        for name in ["flask", "django", "python", "sqlalchemy", "news"]:
            tag = Tag(name=name)
            db.session.add(tag)

        db.session.commit()
        print("Inital dataset is created successfully")
