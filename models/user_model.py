from flask import Blueprint, request, jsonify
#from models.user_model import create_user
from app import mysql


def create_user(name, email, password):
    # Conectar a la base de datos
    cursor = mysql.connection.cursor()

    # Ejecutar consulta para insertar el usuario en la base de datos
    cursor.execute(
        "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
        (name, email, password)
    )

    # Confirmar la transacción
    mysql.connection.commit()

    # Cerrar el cursor
    cursor.close()
