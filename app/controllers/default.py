from flask import render_template
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm

# @app.route() é um decorator, o qual serve para aplicar uma função em cima da outra. A baixo, a função route() é aplicada em cima da função index();
# o método route() define uma rota da minha página

@app.route("/index")
@app.route('/')
def index():
    return render_template('index.html', user=user)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
    else:
        print(form.errors)
    return render_template('login.html', form=form)




# @app.route("/test/<info>")
# @app.route("/test", defaults={'info': None})
# def test(info):
#    # users_list = User.query.filter_by(password='1234').all() # Fazendo um SELECT no db e retornando uma lista de usuários filtrados pelo username. 
#     user = User.query.filter_by(password='1234').first()
#     print(user.username, user.name)
#     return 'Okay'
