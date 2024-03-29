from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app_microblog = Flask(__name__)
app_microblog.config.from_object(Config)
db = SQLAlchemy(app_microblog)
migrate = Migrate(app_microblog, db)
login = LoginManager(app_microblog)
login.login_view = 'login'

from app import routes, models

