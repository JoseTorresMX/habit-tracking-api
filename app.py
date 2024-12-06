# Librerias a usar
# from flask_sqlalchemy import SQLAlchemy
# from flask_restx import Api, Resource, fields, reqparse
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
# from flask import Flask, request, jsonify
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime, timedelta
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
# from sqlalchemy import create_engine

from routes.user_routes import user_routes
from routes.habit_routes import habit_routes
from auth.auth import auth_routes
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mysqldb import MySQL
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

# Inicializar extensiones
CORS(app)
JWTManager(app)
mysql = MySQL(app)

# Registrar las rutas (Blueprints)
app.register_blueprint(habit_routes, url_prefix='/api/habits')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(user_routes, url_prefix='/api/users')

if __name__ == '__main__':
    app.run(debug=True)
