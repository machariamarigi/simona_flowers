"""Main module for our application"""
import os


# 3rd party imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


# local imports
from config import app_config

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):

    if os.getenv('FLASK_CONFIG') == 'production':
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile('config.py')

    # import pdb; pdb.set_trace()
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page"
    login_manager.login_view = "auth.login"

    from .models import User, Category, EventService, Products
    migrate = Migrate(app, db)
    
    Bootstrap(app)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .products import products as products_blueprint
    app.register_blueprint(products_blueprint)

    from .cart import cart as cart_blueprint
    app.register_blueprint(cart_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
