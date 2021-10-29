import os
import functools
from flask import Flask, render_template, jsonify, redirect, request, url_for, flash, session
from markupsafe import escape
from werkzeug.security import generate_password_hash, check_password_hash
from db import consulta, cambios

app=Flask(__name__)

app.secret_key=os.urandom(24)

@app.route('/')
@app.route('/login/', methods=("GET","POST"))
def login():
    try:
        if request.method=="POST":
            session.clear()
            usuario=escape(request.form["usuario"])
            contraseña=escape(request.form["contraseña"])
            #Realizar la consulta en la base de datos de si existe o no el usuario registrado
            consultar=f"Select usuario, contraseña, rol from usuarios where usuario='{usuario}'"
            rta=consulta(consultar)
            if rta!=None:
                if check_password_hash(rta[1],contraseña):
                    session["usuario"]=usuario
                    session["rol"]=rta[2]
                    return redirect(f"/index_{usuario}")
                else:
                    flash("Acceso denegado. Contraseña incorrecta.")
                    return redirect('/')
            else:
                flash(f'El usuario "{usuario}" no existe, debe registrarse.')
                return redirect('/')
        else:
            if session["usuario"]!=None:
                usuario=session["usuario"]
                return redirect(f"/index_{usuario}")
            else:
                return render_template('login.html')
    except:
        return render_template('login.html')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session["usuario"] is None:
            return redirect("/login")
        return view(**kwargs)
    return wrapped_view

@app.route('/index_<nombre_usuario>/', methods=("GET","PUT"))
@login_required
def front_page(nombre_usuario):
    return render_template('frontpage.html')
    
@app.route('/publicacion_<nombre_usuario>/', methods=('GET','POST','PUT','DELETE'))
@login_required
def publicacion(nombre_usuario):
    return render_template('publicacion.html')
    
@app.route('/registro/', methods=("GET","POST"))
def registro():
    try:
        if request.method=="POST":
            #Recuperar los datos del formulario
            nombre=escape(request.form["nombre"])
            apellido=escape(request.form["apellido"])
            usuario=escape(request.form["usuario"])
            correo=escape(request.form["correo"])
            contraseña=escape(request.form["pass1"])
            fecha_nac=escape(request.form["fecha_nac"])
            #Realizar la consulta en la base de datos de si existe o no el usuario registrado y el correo
            consultar=f"Select nombre_usuario, correo_electronico from Informacion_usuarios where nombre_usuario='{usuario}' or correo_electronico='{correo}';"
            #Guardar la consulta
            rta=consulta(consultar)
            if rta==None:
                contra=generate_password_hash(contraseña,method="pbkdf2:sha512")
                insertar=f"Insert into usuarios(usuario, contraseña, rol) Values ('{usuario}','{contra}','Usuario_final');"
                rta=cambios(insertar)
                insertar=f"Insert into Informacion_usuarios(nombre_usuario, nombre, apellido, fecha_nacimiento, correo_electronico) Values ('{usuario}','{nombre}','{apellido}','{fecha_nac}','{correo}');"
                rta=cambios(insertar)
                if rta !=0:
                    return redirect("/login")
            else:
                return redirect(url_for("/registro"))
                if rta[0]==usuario and rta[1]!=correo:
                    flash(f"Ya existe el nombre de usuario: {usuario}. Por favor registre otro")
                elif rta[0]!=usuario and rta[1]==correo:
                    flash(f"El correo electrónico: {correo} ya se encuentra registrado con otro nombre de usuario.")
                else:
                    flash(f"Ya existe el nombre de usuario: {usuario}.\n Y el correo electrónico: {correo} ya está registrado.")
                #return redirect(url_for("/registro"))
        else:
            return render_template('registro.html')
    except:
        return render_template('registro.html')
    
@app.route('/perfil/', methods=('GET','POST','DELETE','PATCH'))
@login_required
def perfil_usuario():
    return render_template('perfil.html')
    
@app.route('/editar_perfil/', methods=('GET','POST','DELETE','PATCH'))
@login_required
def editar_perfil():
    return render_template('editarperfil.html')
    
@app.route('/buscar/')
@login_required
def buscar_usuario():
    return render_template('buscar.html')
    
@app.route('/preguntas_frecuentes/')
def preguntas_frecuentes():
    return render_template('preguntas_frecuentes.html')
    
@app.route('/dashboard/', methods=("GET","POST","PUT","DELETE","PATCH","CONNECT"))
@login_required
def dashboard():
    if session["rol"]=="Administrador":
        return render_template('dashboard.html')
    else:
        usuario=session["usuario"]
        return redirect(f"/index_{usuario}")
        
@app.route('/logout')
def logout():
    # eliminar el nombre de usuario de la sesión si está allí
    session.pop('usuario', None)
    return redirect(url_for('login'))
    
if __name__ =='__main__':
    app.run(port=80, debug=True)