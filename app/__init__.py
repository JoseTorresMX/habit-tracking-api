from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes import main
from app.auth import auth

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config.Config')

    db.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
