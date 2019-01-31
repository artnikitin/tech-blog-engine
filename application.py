from flask import Flask, flash, jsonify, render_template, request, url_for, session, redirect, flash
import datetime

from helpers import *
from passlib.apps import custom_app_context as pwd_context
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from tempfile import mkdtemp

from layout import Layout

app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class Post(db.Model):

    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.Text)
    sub_heading = db.Column(db.Text)
    text = db.Column(db.Text)
    category = db.Column(db.Text)
    url = db.Column(db.Text)
    author = db.Column(db.Text)
    date = db.Column(db.Date)
    published = db.Column(db.Integer)

    def __init__(self, heading, subheading, text, category, url, author, date, published):
        self.heading = heading
        self.sub_heading = subheading
        self.text = text
        self.category = category
        self.url = url
        self.author = author
        self.date = date
        self.published = published

class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    hash = db.Column(db.Text)

    def __init__(self, username, hash):
        self.username = username
        self.hash = hash

@app.route("/")
def index():
    image_url = "/static/img/pixels-1.jpg"
    heading = "Algebra, Statistics and Calculus Tutorials"
    subheading = "an easy-to-reach reference"
    heading_class = "site-heading"
    subheading_class = "span"
    category = request.args.get("")
    box_id = "header_home_box"

    rows = Post.query.order_by(Post.id.desc()).limit(4)

    posts = []
    for object in rows:
        day = int(object.date.strftime("%d"))
        day = str(day)
        date_unformatted = object.date.strftime("%Y-%m-%d")
        today = datetime.datetime.now().strftime("%Y-%m-%d")

        if date_unformatted == today:
            posts.append({object: "Today"})
        else:
            date_formatted = object.date.strftime("%B {}, %Y".format(day))
            posts.append({object: "{}".format(date_formatted)})

    return render_template("index.html", image_url=image_url, heading=heading,
                           subheading=subheading, heading_class=heading_class,
                           subheading_class=subheading_class, posts=posts,
                           category=category, box_id=box_id)

@app.route("/algebra")
def algebra():
    image_url = "/static/img/35839019-math-wallpaper.jpg"
    heading = "Algebra"
    subheading = "high school Algebra I and Algebra II"
    heading_class = "site-heading"
    subheading_class = "span"
    box_id = "header_category_box"

    rows = Post.query.order_by(Post.id.desc()).filter(Post.category == "Algebra")

    posts = []
    for object in rows:
        day = int(object.date.strftime("%d"))
        day = str(day)
        date_unformatted = object.date.strftime("%Y-%m-%d")
        today = datetime.datetime.now().strftime("%Y-%m-%d")

        if date_unformatted == today:
            posts.append({object: "Today"})
        else:
            date_formatted = object.date.strftime("%B {}, %Y".format(day))
            posts.append({object: "{}".format(date_formatted)})

    return render_template("category.html", image_url=image_url, heading=heading,
                           subheading=subheading, heading_class=heading_class,
                           subheading_class=subheading_class, posts=posts, box_id=box_id)

@app.route("/statistics")
def statistics():
    image_url = "/static/img/164662716-python-wallpapers.jpg"
    heading = "Statistics"
    subheading = "stats and probability"
    heading_class = "site-heading"
    subheading_class = "span"
    box_id = "header_category_box"

    rows = Post.query.order_by(Post.id.desc()).filter(Post.category == "Statistics")

    posts = []
    for object in rows:
        day = int(object.date.strftime("%d"))
        day = str(day)
        date_unformatted = object.date.strftime("%Y-%m-%d")
        today = datetime.datetime.now().strftime("%Y-%m-%d")

        if date_unformatted == today:
            posts.append({object: "Today"})
        else:
            date_formatted = object.date.strftime("%B {}, %Y".format(day))
            posts.append({object: "{}".format(date_formatted)})

    return render_template("category.html", image_url=image_url, heading=heading,
                           subheading=subheading, heading_class=heading_class,
                           subheading_class=subheading_class, posts=posts, box_id=box_id)

@app.route("/calculus")
def calculus():
    image_url = "/static/img/data-viz.jpg"
    heading = "Calculus"
    subheading = "integral and differential calculus"
    heading_class = "site-heading"
    subheading_class = "span"
    box_id = "header_category_box"

    rows = Post.query.order_by(Post.id.desc()).filter(Post.category == "Calculus")

    posts = []
    for object in rows:
        day = int(object.date.strftime("%d"))
        day = str(day)
        date_unformatted = object.date.strftime("%Y-%m-%d")
        today = datetime.datetime.now().strftime("%Y-%m-%d")

        if date_unformatted == today:
            posts.append({object: "Today"})
        else:
            date_formatted = object.date.strftime("%B {}, %Y".format(day))
            posts.append({object: "{}".format(date_formatted)})

    return render_template("category.html", image_url=image_url, heading=heading,
                           subheading=subheading, heading_class=heading_class,
                           subheading_class=subheading_class, posts=posts, box_id=box_id)

@app.route("/linear_algebra")
def linear_algebra():
    image_url = "/static/img/data-viz.jpg"
    heading = "Linear Algebra"
    subheading = "matrix manipulation and other cool stuff"
    heading_class = "site-heading"
    subheading_class = "span"
    box_id = "header_category_box"

    rows = Post.query.order_by(Post.id.desc()).filter(Post.category == "Calculus")

    posts = []
    for object in rows:
        day = int(object.date.strftime("%d"))
        day = str(day)
        date_unformatted = object.date.strftime("%Y-%m-%d")
        today = datetime.datetime.now().strftime("%Y-%m-%d")

        if date_unformatted == today:
            posts.append({object: "Today"})
        else:
            date_formatted = object.date.strftime("%B {}, %Y".format(day))
            posts.append({object: "{}".format(date_formatted)})

    return render_template("category.html", image_url=image_url, heading=heading,
                           subheading=subheading, heading_class=heading_class,
                           subheading_class=subheading_class, posts=posts, box_id=box_id)

@app.route("/about")
def about():
    about = Layout("/static/img/8344_1920_1200.jpg", "Where am I?", "",
                   "site-heading", "span", "about.html", "header_category_box")
    return about.render()

@app.route("/post/<url>")
def post(url):

    post = Post.query.filter(Post.url == url).first()

    heading = post.heading
    subheading = post.sub_heading
    heading_class = "post-heading"
    subheading_class = "h2"
    box_id = "header_post_box"

    global date_formatted

    day = int(post.date.strftime("%d"))
    day = str(day)
    date_unformatted = post.date.strftime("%Y-%m-%d")
    today = datetime.datetime.now().strftime("%Y-%m-%d")

    if date_unformatted == today:
        date_formatted = "Today"
    else:
        date_formatted = post.date.strftime("%B {}, %Y".format(day))

    return render_template("post.html", heading=heading,
                           subheading=subheading, heading_class=heading_class,
                           subheading_class=subheading_class, post=post,
                           date_formatted=date_formatted, box_id=box_id)

@app.route("/admin")
@login_required
def admin():
    image_url = "/static/img/garage-by-dengo-1.jpg"
    heading = "Admin"
    subheading = "Where all the magic happens"
    heading_class = "page-heading"
    subheading_class = "span"

    rows = Post.query.order_by(Post.id.desc()).all()
    posts_month = []
    current_month = ""
    current_year = ""
    first_month = True
    first_year = True

    for object in rows:
        month = object.date.strftime("%B")
        year = object.date.strftime("%Y")

        if first_month and first_year:
            posts_month.append({object: [month, year]})
            first_month = False
            first_year = False

        elif month == current_month and year == current_year:
            posts_month.append({object: ["", ""]})

        elif month != current_month and current_month != "" and year == current_year:
            posts_month.append({object: [month, ""]})

        elif year != current_year and current_year != "" and month == current_month:
            posts_month.append({object: ["", year]})

        current_month = month
        current_year = year

    return render_template("admin.html", image_url=image_url, heading=heading,
                           subheading=subheading, heading_class=heading_class,
                           subheading_class=subheading_class, posts_month=posts_month)

@app.route("/archive")
def archive():
    image_url = "/static/img/library-wallpaper-2.jpg"
    heading = "Archive"
    subheading = ""
    heading_class = "page-heading"
    subheading_class = "span"
    box_id = "header_post_box"

    rows = Post.query.order_by(Post.id.desc()).all()
    posts_month = []
    current_month = ""
    current_year = ""
    first_month = True
    first_year = True

    for object in rows:
        month = object.date.strftime("%B")
        year = object.date.strftime("%Y")

        if first_month and first_year:
            posts_month.append({object: [month, year]})
            first_month = False
            first_year = False

        elif month == current_month and year == current_year:
            posts_month.append({object: ["", ""]})

        elif month != current_month and current_month != "" and year == current_year:
            posts_month.append({object: [month, ""]})

        elif year != current_year and current_year != "" and month == current_month:
            posts_month.append({object: ["", year]})

        current_month = month
        current_year = year

    return render_template("archive.html", image_url=image_url, heading=heading,
                           subheading=subheading, heading_class=heading_class,
                           subheading_class=subheading_class, posts_month=posts_month, box_id=box_id)


@app.route("/admin/create", methods=["GET", "POST"])
@login_required
def create():
    image_url = "/static/img/garage-by-dengo-1.jpg"
    heading = "Admin"
    subheading = "Where all the magic happens"
    heading_class = "page-heading"
    subheading_class = "span"

    if request.method == "POST":
            if request.form.get("publish") == "publish":
                heading = request.form["heading"]
                subheading = request.form["subheading"]
                text = request.form["text"]
                author = request.form["author"]
                category = request.form["category"]
                url = slugify(heading)
                date = datetime.datetime.now()
                published = 1

                post = Post(heading, subheading, text, category,
                            url, author, date, published)

                db.session.add(post)
                db.session.commit()
                flash("post published")
                return redirect(url_for("admin"))

            if request.form.get("save") == "save":
                heading = request.form["heading"]
                subheading = request.form["subheading"]
                text = request.form["text"]
                author = request.form["author"]
                category = request.form["category"]
                url = slugify(heading)
                date = datetime.datetime.now()
                published = 0

                post = Post(heading, subheading, text, category,
                            url, author, date, published)

                db.session.add(post)
                db.session.commit()
                flash("post saved")
                return redirect(url_for("admin"))

            if request.form.get("preview") == "preview":
                post = Post.query.filter(Post.heading == request.form['heading']).all()
                if post == []:
                    return redirect(url_for("create"))
                else:
                    return redirect(url_for("post", url=post[0].url))
    else:
        return render_template("create.html", image_url=image_url, heading=heading,
                               subheading=subheading, heading_class=heading_class,
                               subheading_class=subheading_class)

@app.route("/admin/edit")
@login_required
def edit():
    image_url = "/static/img/garage-by-dengo-1.jpg"
    heading = "Admin"
    subheading = "Where all the magic happens"
    heading_class = "page-heading"
    subheading_class = "span"

    post_heading = request.args.get("post_heading")
    print(post_heading)
    post = Post.query.filter(Post.heading == post_heading).all()
    print(post)

    return render_template("edit.html", image_url=image_url, heading=heading,
                            subheading=subheading, heading_class=heading_class,
                            subheading_class=subheading_class, post=post)

@app.route("/admin/edit", methods=["POST"])
@login_required
def update():
        if request.form["heading"] and request.form["subheading"] and request.form["text"]:
            if request.form.get("save") == "save":
                post = Post.query.filter(Post.id == request.form["id"]).all()
                print(post)
                print(request.form["id"])
                post[0].heading = request.form["heading"]
                post[0].url = slugify(request.form["heading"])
                post[0].sub_heading = request.form["subheading"]
                post[0].text = request.form["text"]
                post[0].author = request.form["author"]
                post[0].category = request.form["category"]

                db.session.commit()
                flash("post saved")
                return redirect(url_for("admin"))

            if request.form.get("preview") == "preview":
                post = Post.query.filter(Post.id == request.form["id"]).all()
                return redirect(url_for("post", url=post[0].url))

            if request.form.get("publish") == "publish":
                post = Post.query.filter(Post.id == request.form["id"]).all()
                post[0].published = 1
                db.session.commit()
                flash("post published")
                return redirect(url_for("admin"))

            if request.form.get("unpublish") == "unpublish":
                post = Post.query.filter(Post.id == request.form["id"]).all()
                post[0].published = 0
                db.session.commit()
                flash("post unpublished")
                return redirect(url_for("admin"))

            if request.form.get("delete") == "delete":
                Post.query.filter(Post.id == request.form["id"]).delete()
                db.session.commit()
                flash("post deleted")
                return redirect(url_for("admin"))

@app.route("/login", methods=["GET", "POST"])
def login():
    # forget any user_id
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return redirect(url_for("login"))

            # ensure password was submitted
        elif not request.form.get("password"):
            return redirect(url_for("login"))

        rows = User.query.filter(User.username == request.form.get("username")).first()

        if rows.username == None or not pwd_context.verify(request.form.get("password"), rows.hash):
            return redirect(url_for("login"))

        # remember which user has logged in
        session["user_id"] = rows.id

        # redirect user to admin
        return redirect(url_for("admin"))

    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()



