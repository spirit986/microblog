from flask import Flask
from config import Config

app_microblog = Flask(__name__)
app_microblog.config.from_object(Config)

from app import routes
