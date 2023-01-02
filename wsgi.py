from app import create_app, db
from app.models import User

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        # "Article": Article,
    }


if __name__ == "__main__":
    app.run(host="localhost", port="5001", debug=True)
