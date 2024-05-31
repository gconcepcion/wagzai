from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from wagzai.extensions import (  # Import the login_manager instance here
    db,
    login_manager,
)
from wagzai.forms import LoginForm, RegistrationForm
from wagzai.models import User
from wagzai.nlp import process_query

app_blueprint = Blueprint("app", __name__, template_folder="templates")

login_manager.init_app(app_blueprint)  # Initialize the login manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for("app.login"))
    return render_template("register.html", title="Register", form=form)


@app_blueprint.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if user and user.check_password(form.password.data):
            login_user(user)  # Call login_user directly from Flask-Login
            flash("Login successful!", "success")
            return redirect(url_for("app.dashboard"))
        else:
            flash("Login unsuccessful. Please check your email and password.", "danger")
    return render_template("login.html", title="Log In", form=form)


@app_blueprint.route("/logout")
@login_required  # Add login_required decorator
def logout():
    logout_user()  # Call logout_user directly from Flask-Login
    flash("You have been logged out!", "info")
    return redirect(url_for("app.index"))


@app_blueprint.route("/dashboard")
@login_required  # Add login_required decorator
def dashboard():
    return render_template("dashboard.html", title="Dashboard")


@app_blueprint.route("/")
def index():
    return render_template("index.html", title="Home")


@app_blueprint.route("/about")
def about():
    return render_template("about.html", title="About")


@app_blueprint.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")


@app_blueprint.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    return render_template("index.html")


@app_blueprint.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        # Your logic here to handle POST requests
        #     print(request.data)
        #    test = request.data.decode('utf-8')
        #     print(request.data.decode('utf-8'))
        resp = process_query(request.data.decode("utf-8"))
        print(resp)
        return jsonify({"message": resp})

    return render_template("chat.html", title="Chat")
