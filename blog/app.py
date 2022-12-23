from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "index page"


@app.route("/<string:message>")
def print_some_message(message: str = "default text"):
    return f"some message: {message}"


@app.errorhandler(404)
def not_found(error):
    app.logger.error(error)
    return '404'