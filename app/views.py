# app/views.py

from flask import Flask, render_template
from flask_login import LoginManager, login_required

# local imports
from config import app_config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config['development'])
app.config.from_pyfile('config.py')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "login"

    
@app.route('/')
def index():
    return render_template("index.html", title="Welcome")

@app.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template("dashboard.html", title="Dashboard")