#from flask import Blueprint, request, jsonify
#from models.user_model import create_user
from app import mysql
#from flask_mysqldb import MySQL
from flask_mysqldb import MySQL

def create_user(mysql, name, email, password):
    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (name, email, password)
    )
    mysql.connection.commit()
    cursor.close()

def get_users(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    cursor.close()
    return users

