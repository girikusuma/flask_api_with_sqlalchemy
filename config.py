import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USER = str(os.environ.get("DB_USER"))
    PASS = str(os.environ.get("DB_PASS"))

    JWT_SECRET_KEY =  str(os.environ.get("JWT_SECRET"))

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + USER + ':' + PASS + '@' + HOST + '/' + DATABASE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True