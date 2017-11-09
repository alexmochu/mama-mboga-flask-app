# app/views.py

from flask import Flask, render_template, url_for, flash
from flask_login import LoginManager, login_required, current_user, login_user
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect

# local imports
from config import app_config
from app.exceptions import ShoppingListAlreadyExist, ItemAlreadyExist, \
    ShoppingListDoesNotExist, ItemDoesNotExist
from app.forms import SignUpForm, LoginForm
from app.models.accounts import Accounts
from app.models.user import User

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config['development'])
app.config.from_pyfile('config.py')

accounts = Accounts()
login_manager = LoginManager()
Bootstrap(app)
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "/login"

    
@app.route('/')
def index():
    return render_template("index.html", title="Welcome")

@login_manager.user_loader
def load_user(email):
    return accounts.check_user(email)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if current_user.is_authenticated:
        return render_template("dashboard.html")
    else:
        return redirect(url_for("login"))

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    global accounts
    form = SignUpForm()

    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    else:
        if form.validate_on_submit():
            if accounts.check_user(form.email.data):
                flash("User already exists", "info")
            else:
                accounts.add_user(
                    User(form.username.data, form.email.data, form.password.data))
                flash("User Created Successfully", "success")
                return redirect("login")

    return render_template("signup.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    """
    Login endpoint for registered users
    :return: 
    """
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    else:
        if form.validate_on_submit():
            user = accounts.check_user(form.email.data)
            if user:
                # A User Exist with that Email now check password
                if user.verify_password(form.password.data):
                    login_user(user)
                    return redirect(url_for('dashboard'))
                else:
                    flash("Invalid Username Or Password", 'danger')
            else:
                flash("User Does Not Exist", 'danger')

    return render_template("login.html", form=form)




