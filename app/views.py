# app/views.py

from flask import Flask, render_template

# local imports
from config import app_config

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(app_config['development'])
app.config.from_pyfile('config.py')
    
@app.route('/')
def index():
    return render_template("index.html")