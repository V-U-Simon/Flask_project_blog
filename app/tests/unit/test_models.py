from app.models import User, Author, Article, Tag
from app import db


def test_user(db, users):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, hashed_password, authenticated, fields are defined correctly
    """
    
    assert User.active.count() == 4
    user = User.query.filter_by(username='user_1').first()
    assert user.email == "user_1@example.com"
    assert user.password_hash != "passwd"
    assert user.check_password("passwd") == True

    assert user.is_staff != True
    user.is_staff = True
    db.session.add(user)
    db.session.commit()
    assert user.is_staff == True

    db.session.delete(user)
    db.session.commit()
    assert User.active.count() == 3


def test_user_alternative_deleting(users):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, set_password, check_password, authenticated, and role fields are defined correctly
    """
    user = User.query.filter_by(username='user_1').first()
    
    assert user.query.count() == 4
    assert user.deleted.count() == 0
    user.is_deleted != True
    user.delete()
    user.is_deleted == True
    assert user.active.count() == 3
    assert user.deleted.count() == 1
    user.recover()
    user.is_deleted != True
    assert user.query.count() == 4
    assert user.deleted.count() == 0


def test_author(users):
    user_author = User.query.filter_by(username='user_1').first()
    
    user_author.set_as_author()
    db.session.commit()
    assert user_author.is_author == True
    
    user_author.unset_as_author()
    db.session.commit()
    assert user_author.is_author != True


def test_author_article(article: Article):
    assert article.query.count() == 1
    assert article.arhive.count() == 0
    assert article.published.count() == 1
    article.delete()
    assert article.query.count() == 1
    assert article.arhive.count() == 1
    assert article.published.count() == 0
    article.recover()
    assert article.query.count() == 1
    assert article.arhive.count() == 0
    assert article.published.count() == 1


def test_tags(db, articles):
    for article in articles:
        assert article.tag_exists() != True

        tag = Tag(name="some_tag")
        
        article.add_tag(tag)
        db.session.commit()
        assert article.tag_exists() == True
        
        article.remove_tag(tag)
        db.session.commit()
        assert article.tag_exists() != True


def test_author_article(users):
    user_author = list(filter(lambda user: user.is_author, users))[0]
    author = user_author.author
   
    article = Article(
            title=f"My title number 1",
            body="Some text will be here for article number 1",
        )
    
    author.add_article(article)
    db.session.commit()
    assert author.has_articles() == True
    assert author.articles.count() == 1

    author.remove_article(article)
    db.session.commit()
    assert author.has_articles() == False
    assert article.query.count() == 1  # save but not published
    assert article.published.count() == 0  # save but not published


def test_get_one_article(articles: db.Query):
    """
    GIVEN list of articles
    WHEN get details information for definetly article
    THEN get one article by ID from oter article list
    """
    article = articles.get(1)
    assert article.id == 1
