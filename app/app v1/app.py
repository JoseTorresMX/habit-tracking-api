# app.py

from flask import Flask
from flask_mysqldb import MySQL
# from routes import app
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mysql = MySQL(app)


@app.route('/')
def home():
    return "API de Seguimiento de Hábitos por Jose Torres"

# Ruta para probar la conexión a la base de datos
@app.route('/test-db', methods=['GET'])
def test_db():
    try:
        # Intentamos ejecutar una consulta de prueba
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT 1')
        result = cursor.fetchone()
        cursor.close()
        return f'Conexión a la base de datos exitosa: {result}'
    except Exception as e:
        return f'Error de conexión: {e}'


if __name__ == '__main__':
    app.run(debug=True)
