import logging.handlers
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from config import Config

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s - %(message)s")
handler = logging.handlers.RotatingFileHandler(
        '/var/log/azgar/app.log',
        maxBytes=1024 * 1024)
handler.setFormatter(formatter)
access_log_handler = logging.FileHandler('/var/log/azgar/access.log')

logging.getLogger('werkzeug').setLevel(logging.DEBUG)
logging.getLogger('werkzeug').addHandler(access_log_handler)

app.logger.setLevel(logging.INFO)
app.logger.addHandler(handler)

from azgar import views, models