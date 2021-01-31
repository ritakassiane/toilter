from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app) # criando o banco de dados 
migrate = Migrate(app, db) # Cuidará das migrações

manager = Manager(app) # Cuida dos comandos que iremos dar para inicializar a aplicação 
manager.add_command('db', MigrateCommand) 

from app.models import tables
from app.controllers import default

