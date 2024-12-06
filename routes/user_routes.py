from flask import Blueprint, request, jsonify, current_app
#from models import create_user, get_user
user_routes = Blueprint('users', __name__)


@user_routes.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    # Validar si los datos existen
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'message': 'Todos los campos son requeridos'}), 400

    try:
        mysql = current_app.extensions.get('mysql', None)

        if mysql is None:
            return jsonify({'message': 'Error en la conexión a la base de datos'}), 500

        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
            (name, email, password)
        )
        mysql.connection.commit()
        cursor.close()

        return jsonify({'message': 'Usuario registrado con éxito'}), 201

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'message': 'Error en la conexion a la base de datos'}), 500


@user_routes.route('/all', methods=['GET'])
def get_users():
    mysql = current_app.extensions.get('mysql', None)

    if mysql is None:
        return jsonify({'message': 'Error en la conexión a la base de datos'}), 500

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    cursor.close()

    # Convertir los resultados a una lista de diccionarios
    users_list = []
    for user in users:
        users_list.append({
            'id': user[0],
            'name': user[1],
            'email': user[2]
        })

    return jsonify(users_list), 200
