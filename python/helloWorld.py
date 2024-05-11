from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "index page"


@app.route("/hello")
def hello():
    return "Hello, World"


@app.route("/user/<username>")
def show_user_profile(username):
    # show thie user profile for that user
    return f"User {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show thie post with the given id, the id is an integer
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # show the subpath after /path/
    return f"Subpath {escape(subpath)}"


app.run()
