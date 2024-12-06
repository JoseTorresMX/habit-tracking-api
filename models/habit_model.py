from flask import Blueprint, request, jsonify
from models.habit_model import create_habit, get_all_habits, get_habit_by_id, update_habit, delete_habit

habit_routes = Blueprint('habits', __name__)


@habit_routes.route('/', methods=['POST'])
def add_habit():
    data = request.get_json()
    name = data.get('name')
    date = data.get('date')
    status = data.get('status')

    if not name or not date or not status:
        return jsonify({'message': 'Todos los campos son requeridos'}), 400

    create_habit(name, date, status)
    return jsonify({'message': 'Hábito creado con éxito'}), 201


@habit_routes.route('/', methods=['GET'])
def get_habits():
    habits = get_all_habits()
    return jsonify(habits)


@habit_routes.route('/<int:habit_id>', methods=['GET'])
def get_habit(habit_id):
    habit = get_habit_by_id(habit_id)
    if habit:
        return jsonify(habit)
    return jsonify({'message': 'Hábito no encontrado'}), 404


@habit_routes.route('/<int:habit_id>', methods=['PUT'])
def update_existing_habit(habit_id):
    data = request.get_json()
    name = data.get('name')
    date = data.get('date')
    status = data.get('status')

    if not name or not date or not status:
        return jsonify({'message': 'Todos los campos son requeridos'}), 400

    update_habit(habit_id, name, date, status)
    return jsonify({'message': 'Hábito actualizado con éxito'})


@habit_routes.route('/<int:habit_id>', methods=['DELETE'])
def delete_existing_habit(habit_id):
    delete_habit(habit_id)
    return jsonify({'message': 'Hábito eliminado con éxito'})
