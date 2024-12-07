from flask import Flask
from flask_jwt_extended import JWTManager
from .models import db, bcrypt
from .routes import habits_bp
from .auth import auth_bp
from config import Config


def create_app():
    app = Flask(__name__)

    # Cargar cnfiguraciones
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    bcrypt.init_app(app)
    jwt = JWTManager(app)

    # Registrar blueprints
    app.register_blueprint(habits_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app
