# models.py

from flask_mysqldb import MySQL
from config import Config

def get_db_connection():
    # Conectar a la base de datos MySQL
    mysql = MySQL()
    mysql.init_app(Config)
    return mysql.connection

def create_habit(name, date, status):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO habits (name, date, status) VALUES (%s, %s, %s)", (name, date, status))
    connection.commit()
    cursor.close()

def get_all_habits():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM habits")
    habits = cursor.fetchall()
    cursor.close()
    return habits

def get_habit_by_id(habit_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM habits WHERE id = %s", [habit_id])
    habit = cursor.fetchone()
    cursor.close()
    return habit

def update_habit(habit_id, name, date, status):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE habits SET name = %s, date = %s, status = %s WHERE id = %s", (name, date, status, habit_id))
    connection.commit()
    cursor.close()

def delete_habit(habit_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM habits WHERE id = %s", [habit_id])
    connection.commit()
    cursor.close()
