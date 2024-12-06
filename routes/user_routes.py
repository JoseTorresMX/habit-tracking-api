from flask import Blueprint, request, jsonify, current_app

user_routes = Blueprint('users', __name__)


@user_routes.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    name = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Verificar que los campos no estén vacíos
    if not name or not email or not password:
        return jsonify({'message': 'Todos los campos son requeridos'}), 400

    # Usar current_app para acceder a mysql
    mysql = current_app.extensions.get('mysql', None)

    if mysql is None:
        return jsonify({'message': 'Error en la conexión a la base de datos'}), 500

    # Conectar y registrar el usuario en la base de datos
    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
        (name, email, password)
    )
    mysql.connection.commit()
    cursor.close()

    return jsonify({'message': 'Usuario registrado con éxito'}), 201
