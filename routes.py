# routes.py

from flask import Flask, request, jsonify
from models import create_habit, get_all_habits, get_habit_by_id, update_habit, delete_habit

app = Flask(__name__)

@app.route('/habit/', methods=['POST'])
def add_habit():
    data = request.get_json()
    name = data['name']
    date = data['date']
    status = data['status']
    
    create_habit(name, date, status)
    
    return jsonify({'message': 'Hábito agregado correctamente'}), 201

@app.route('/habits/', methods=['GET'])
def get_habits():
    habits = get_all_habits()
    habit_list = []
    for habit in habits:
        habit_list.append({
            'id': habit[0],
            'name': habit[1],
            'date': habit[2],
            'status': habit[3]
        })
    return jsonify(habit_list), 200

@app.route('/habit/<int:habit_id>/', methods=['GET'])
def get_habit(habit_id):
    habit = get_habit_by_id(habit_id)
    if habit:
        return jsonify({
            'id': habit[0],
            'name': habit[1],
            'date': habit[2],
            'status': habit[3]
        }), 200
    return jsonify({'message': 'Hábito no encontrado'}), 404

@app.route('/habit/<int:habit_id>/', methods=['PUT'])
def update_habit_route(habit_id):
    data = request.get_json()
    name = data['name']
    date = data['date']
    status = data['status']
    
    update_habit(habit_id, name, date, status)
    return jsonify({'message': 'Hábito actualizado correctamente'}), 200

@app.route('/habit/<int:habit_id>/', methods=['DELETE'])
def delete_habit_route(habit_id):
    delete_habit(habit_id)
    return jsonify({'message': 'Hábito eliminado correctamente'}), 200
