import os


class Config:
    SECRET_KEY = os.getenv(
        'SECRET_KEY', 'eee20be563f78d42d7a29c19cecd844b3e40be6fb49ae49a17ac651cde736b4c')
    SQLALCHEMY_DATABASE_URI = 'mysql://jtorres:123456789@localhost/habit_tracker'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
