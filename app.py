from flask import Flask, request, jsonify
import jwt
import mysql.connector
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eee20be563f78d42d7a29c19cecd844b3e40be6fb49ae49a17ac651cde736b4c'

# Configurar conexión a MySQL
db = mysql.connector.connect(
    host="localhost",
    user="jtorres",
    password="123456789",
    database="habit_tracker"
)


@app.route('/register_habit', methods=['POST'])
def register_habit():
    data = request.get_json()
    habit_name = data['name']
    habit_date = data['date']
    habit_status = data['status']

    cursor = db.cursor()
    query = "INSERT INTO habits (name, date, status) VALUES (%s, %s, %s)"
    cursor.execute(query, (habit_name, habit_date, habit_status))
    db.commit()
    return jsonify({"message": "Habit registered successfully"}), 201


@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if auth and auth.username == 'user' and auth.password == 'pass':
        token = jwt.encode({
            'user': auth.username,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401


if __name__ == '__main__':
    app.run(debug=True)
