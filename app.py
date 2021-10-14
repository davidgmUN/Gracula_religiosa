import os
from flask import Flask, render_template

app=Flask(__name__)

app.secret_key=os.urandom(24)

@app.route('/', methods=['GET','POST'])
def login():
    return render_template('login.html')
    
@app.route('/index', methods=['GET','PUT'])
def front_page():
    return render_template('frontpage.html')
    
@app.route('/publicacion', methods=['GET','POST','PUT','DELETE'])
def publicacion():
    return render_template('publicacion.html')
    
@app.route('/registro', methods=['GET','POST'])
def registro():
    return render_template('registro.html')
    
@app.route('/perfil', methods=['GET','POST','DELETE','PATCH'])
def perfil_usuario():
    return render_template('perfil.html')
    
@app.route('/buscar', methods=['GET'])
def buscar_usuario():
    return render_template('busqueda_Usuario.html')
    
@app.route('/preguntas_frecuentes', methods=['GET'])
def preguntas_frecuentes():
    return render_template('preguntas_frecuentes.html')
    
@app.route('/dashboard', methods=['GET','POST','PUT','DELETE','PATCH','CONNECT'])
def dashboard():
    return render_template('dashboard.html')