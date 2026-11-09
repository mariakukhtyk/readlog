from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required
from cs50 import SQL


app = Flask(__name__)

app.secret_key = "supersecretkey"

db = SQL("sqlite:///readlog.db")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Перевірка імені користувача
        if not username:
            return apology("must provide username", 400)

        # Перевірка пароля
        elif not password:
            return apology("must provide password", 400)

        # Перевірка збігу паролів
        elif not confirmation or password != confirmation:
            return apology("passwords must match", 400)

        # Перевірка, чи існує вже такий користувач
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) > 0:
            return apology("username already exists", 400)

        # Хешування пароля та збереження в базу даних
        hash_val = generate_password_hash(password)
        user_id = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, hash_val)

        # Автоматичний вхід користувача в систему
        session["user_id"] = user_id

        # Перенаправлення на головну сторінку
        return redirect("/")

    # GET request handler — MUST return template
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/")
@login_required
def index():
    """Show user's book reading log"""
    # Query database for books belonging to the logged-in user
    books = db.execute(
        "SELECT * FROM books WHERE user_id = ?", session["user_id"]
    )
    return render_template("index.html", books=books)

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Add a book to the reading log"""

    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        status = request.form.get("status")
        total_pages = request.form.get("total_pages")

        # Basic validation
        if not title:
            return apology("must provide book title", 400)
        if not author:
            return apology("must provide author", 400)
        if not status:
            return apology("must provide reading status", 400)
        if not total_pages:
            total_pages = 0

        # Insert book into database for the current user
        db.execute(
            "INSERT INTO books (user_id, title, author, status, total_pages) VALUES (?, ?, ?, ?, ?)",
            session["user_id"], title, author, status, total_pages
        )

        flash("Book added successfully!")
        return redirect("/")

    else:
        return render_template("add_book.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Clear user session
    session.clear()

    # Redirect user to login form
    return redirect("/")