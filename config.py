import os


basedir = os.path.abspath(os.path.dirname(__file__))  # Obtengo el path actual


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' \
        + os.path.join(basedir, 'app.db')  # Da el path de la db a Flask-SQLAlc
    SQLALCHEMY_TRACK_MODIFICATIONS = False
