from app import create_app, db


app = create_app()


@app.shell_context_processor
def make_shell_context():
    from pprint import pprint
    from app.models import User, Author, Article, Tag

    return {
        "pprint": pprint,
        "db": db,
        "User": User,
        "Author": Author,
        "Article": Article,
        "Tag": Tag,

    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
