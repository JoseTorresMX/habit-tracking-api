from flask import Blueprint, request, jsonify
from app.models import Habit
from app.auth import token_required

# Definir el Blueprint
main = Blueprint('main', __name__)

@main.route('/register_habit', methods=['POST'])
@token_required
def register_habit():
    data = request.get_json()
    current_user = get_current_user(request)

    new_habit = Habit(
        user_id=current_user.id,
        name=data['name'],
        date=data['date'],
        status=data['status']
    )
    new_habit.save()

    return jsonify({"message": "Habit registered successfully"}), 201

def get_current_user(request):
    token = request.headers.get('x-access-token')
    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
    return User.query.get(data['user_id'])
