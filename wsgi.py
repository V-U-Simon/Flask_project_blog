from flask import Flask
from blog.app import blog
from user.app import user
from article.app import article


app = Flask(__name__)

if __name__ == "__main__":

    app.register_blueprint(blog, url_prefix="/blog")
    app.register_blueprint(user, url_prefix="/user")
    app.register_blueprint(article, url_prefix="/article")

    app.run(host="localhost", port="5001", debug=True)
