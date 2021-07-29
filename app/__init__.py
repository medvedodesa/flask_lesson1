from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)


from app.menu import bp as menu_bp
app.register_blueprint(menu_bp, url_prefix='/menu')

from app.home import bp as home_bp
app.register_blueprint(home_bp)

app.static_folder = 'static'