from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .models import db, User, bcrypt
from marshmallow import Schema, fields, validate, ValidationError

# Definir el Blueprint antes de usarlo
auth_bp = Blueprint('auth', __name__)


class UserSchema(Schema):
    username = fields.Str(required=True, validate=[
        validate.Length(
            min=3, max=50, error="Username must be between 3 and 50 characters")
    ])
    email = fields.Email(required=True, validate=[
        validate.Length(
            max=100, error="Email must be less than 100 characters")
    ])
    password = fields.Str(required=True, validate=[
        validate.Length(
            min=8, error="Password must be at least 8 characters long")
    ])


user_schema = UserSchema()


@auth_bp.route('/register', methods=['POST'])
def register():
    # Verificar que se envió JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    # Validación de esquema
    try:
        # Valida todos los campos
        validated_data = user_schema.load(data)
    except ValidationError as err:
        # Devuelve todos los errores de validación
        return jsonify({
            "error": "Validation Error",
            "messages": err.messages
        }), 400

    # Verificar campos específicos
    if not all([
        data.get('username'),
        data.get('email'),
        data.get('password')
    ]):
        return jsonify({
            "error": "Missing username, email, or password"
        }), 400

    # Verificar si el usuario ya existe
    existing_user = User.query.filter(
        (User.username == data['username']) | (User.email == data['email'])
    ).first()

    if existing_user:
        return jsonify({
            "error": "Username or email already exists"
        }), 400

    # Crear nuevo usuario
    new_user = User(
        username=data['username'],
        email=data['email']
    )
    new_user.set_password(data['password'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "username": new_user.username,
            "email": new_user.email
        }
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    # Verificar que se envió JSON
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    # Verificar campos
    if not data.get('username') or not data.get('password'):
        return jsonify({"error": "Missing username or password"}), 400

    # Buscar usuario
    user = User.query.filter_by(username=data['username']).first()

    # Verificar credenciales
    if user and user.check_password(data['password']):
        # Crear token de acceso
        access_token = create_access_token(identity=str(user.id))
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Invalid credentials"}), 401


@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    return jsonify({"message": "Endpoint not implemented"}), 501
