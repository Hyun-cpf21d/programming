import os

BASE_DIR = os.path.dirname(__file__)

JWT_SECRET_KEY = "I'M IML"
SECRET_KEY =os.environ['SECRET_KEY']
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI'].format(os.path.join(BASE_DIR, 'app.db'))
# SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']
