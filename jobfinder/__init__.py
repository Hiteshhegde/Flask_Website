from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



# Initializing Flask instance
app = Flask(__name__)

# Database url
DATABASE_URL = "postgresql://root:root@localhost:5432/rootdb"

# Config settings for the flask app
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde'
app.config['APP_SETTINGS'] = "config.DevelopmentConfig"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database for the flask app
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from jobfinder import urls