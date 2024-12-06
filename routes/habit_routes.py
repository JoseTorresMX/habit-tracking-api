from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity



habit_routes = Blueprint('habits', __name__)


@habit_routes.route('/', methods=['POST'])
@jwt_required()
def create_habit():
    data = request.get_json()
    user_id = get_jwt_identity()
    name = data.get('name')
    date = data.get('date')

    if not name or not date:
        return jsonify({'message': 'Nombre y fecha son requeridos'}), 400

    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO habits (user_id, name, date) VALUES (%s, %s, %s)",
        (user_id, name, date)
    )
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Hábito creado con éxito'}), 201


@habit_routes.route('/', methods=['GET'])
@jwt_required()
def get_habits():
    user_id = get_jwt_identity()
    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT id, name, date, status FROM habits WHERE user_id = %s",
        (user_id,)
    )
    habits = cursor.fetchall()
    cursor.close()

    habit_list = [
        {'id': row[0], 'name': row[1], 'date': str(row[2]), 'status': row[3]}
        for row in habits
    ]
    return jsonify(habit_list), 200


@habit_routes.route('/<int:habit_id>', methods=['PATCH'])
@jwt_required()
def update_habit(habit_id):
    data = request.get_json()
    status = data.get('status')

    if status not in ['pending', 'completed']:
        return jsonify({'message': 'Estado inválido'}), 400

    cursor = mysql.connection.cursor()
    cursor.execute(
        "UPDATE habits SET status = %s WHERE id = %s",
        (status, habit_id)
    )
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Estado del hábito actualizado'}), 200


@habit_routes.route('/<int:habit_id>', methods=['DELETE'])
@jwt_required()
def delete_habit(habit_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM habits WHERE id = %s", (habit_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Hábito eliminado'}), 204
