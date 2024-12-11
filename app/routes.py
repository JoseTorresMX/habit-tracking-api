from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import db, Habit, HabitTracking
from datetime import datetime

habits_bp = Blueprint('habits', __name__)


@habits_bp.route('/habits', methods=['POST'])
@jwt_required()
def create_habit():
    current_user_id = get_jwt_identity()
    data = request.get_json()

    # Validar datos de entrada
    """if not data or not data.get('name'):
        return jsonify({'error': 'Falta el nombre del hábito'}), 400"""

    if not data.get('name'):
        return jsonify({"error": "Habit name is required"}), 400
    if not data.get('description'):
        return jsonify({"error": "Habit description is required"}), 400

    try:
        # Obtener el usuario actual desde el JWT
        current_user_id = get_jwt_identity()

        # Crear un nuevo hábito
        new_habit = Habit(
            name=data['name'],
            description=data['description'],
            user_id=current_user_id
        )

        # Añadir y guardar en la base de datos
        db.session.add(new_habit)
        db.session.commit()

        return jsonify({
            "message": "Habit created successfully",
            "habit": {
                "id": new_habit.id,
                "name": new_habit.name,
                "description": new_habit.description
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    """new_habit = Habit(
        user_id=current_user_id,
        name=data['name'],
        description=data.get('description', '')
    )

    db.session.add(new_habit)
    db.session.commit()

    return jsonify({
        "id": new_habit.id,
        "name": new_habit.name,
        "description": new_habit.description
    }), 201"""


@habits_bp.route('/habits', methods=['GET'])
@jwt_required()
def get_habit():
    current_user_id = get_jwt_identity()
    habits = Habit.query.filter_by(user_id=current_user_id).all()

    if not habits:
        return jsonify({'error': 'No se encontraron hábitos'}), 404

    return jsonify([{
        "id": habit.id,
        "name": habit.name,
        "description": habit.description
    }for habit in habits]), 200


@habits_bp.route('/habits/<int:habit_id>/track', methods=['POST'])
@jwt_required()
def track_habit(habit_id):
    current_user_id = get_jwt_identity()
    data = request.get_json()

    # Verificar que el habito pertenece al usuario actual
    habit = Habit.query.filter_by(
        id=habit_id, user_id=current_user_id).first()
    if not habit:
        return jsonify({'error': 'Hábito no encontrado'}), 404

    # Validar fecha y estado
    date_str = data.get('date', datetime.now().date().isoformat())
    status = data.get('status', 'pendiente')

    if status not in ['completado', 'pendiente']:
        return jsonify({'error': f"Estado inválido. Los estados válidos son: 'completado', 'pendiente'"}), 400

    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Fecha inválida'}), 400

    # Crear o actulizar registro se seguimiento
    tracking = HabitTracking.query.filter_by(
        habit_id=habit_id, date=date).first()

    if tracking:
        tracking.status = status
    else:
        tracking = HabitTracking(
            habit_id=habit_id, date=date, status=status)
        db.session.add(tracking)

    db.session.commit()

    return jsonify({
        "habit_id": habit.id,
        "date": date.isoformat(),
        "status": status
    }), 201


"""@habits_bp.route('/habits/<int:habit_id>/tracking', methods=['GET'])
@jwt_required()
def get_habit_tracking(habit_id):
    current_user_id = get_jwt_identity()

    # Verificar que el habito pertenesta al usuasrio actual
    habit = Habit.query.filter_by(id=habit_id, user_id=current_user_id).first()

    if not habit:
        return jsonify({'error': 'Hábito no encontrado'}), 404

    # Obtener registros de seguimiento
    tracking_records = HabitTracking.query.filter_by(habit_id=habit_id).all()

    return jsonify([{
        "date": record.date.isoformat(),
        "status": record.status
    } for tracking in tracking_records]), 200
"""


@habits_bp.route('/habits/<int:habit_id>/tracking', methods=['GET'])
@jwt_required()
def get_habit_tracking(habit_id):
    current_user_id = get_jwt_identity()

    # Verificar que el hábito pertenezca al usuario actual
    habit = Habit.query.filter_by(id=habit_id, user_id=current_user_id).first()

    if not habit:
        return jsonify({'error': 'Hábito no encontrado'}), 404

    # Obtener registros de seguimiento
    tracking_records = HabitTracking.query.filter_by(habit_id=habit_id).all()

    return jsonify([{
        "date": tracking.date.isoformat(),
        "status": tracking.status
    } for tracking in tracking_records]), 200
