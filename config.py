import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or 'a743d8bd15023502bd5cbadde6ef563c22b120b1541b6e80ce5604507f8e84c7'

    # Configuracion de la base de datos MySQL
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.environ.get('DB_USER', 'root')}:"  # Usuario
        f"{os.environ.get('DB_PASSWORD', '')}@"  # password
        f"{os.environ.get('DB_HOST', 'localhost')}/"  # Servidor
        f"{os.environ.get('DB_NAME', 'habit_tracker')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuracion de JWT
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
