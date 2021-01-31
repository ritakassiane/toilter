import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

basedir = os.path.join(basedir, 'storage.db')
DEBUG = True
SQLALCHEMY_DATABASE_URI =  'sqlite+pysqlite:///storage.db'
# SQLALCHEMY_TRACK_MODIFICATIONS vai ser desabilitada no futuro, por isso gera um warning no terminal ao executar a aplicação
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '1234567890'