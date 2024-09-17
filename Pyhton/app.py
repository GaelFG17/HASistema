from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
import numpy as np
import uuid
import pymysql 


#app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:G170122fg#@localhost/Cuest'
db = SQLAlchemy(app)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False) 
    fecha_registro = db.Column(db.DateTime, default=db.func.current_timestamp())

class Preguntas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.Enum('Activo', 'Reflexivo', 'Teórico', 'Pragmático'), nullable=False)

class OpcionesRespuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Integer, nullable=False)

class Respuestas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    id_pregunta = db.Column(db.Integer, db.ForeignKey('preguntas.id'), nullable=False)
    id_opcion = db.Column(db.Integer, db.ForeignKey('opciones_respuesta.id'), nullable=False)
    folio = db.Column(db.String(100), nullable=False)  # Campo de folio único

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')

        # Crear o buscar al usuario
        usuario = Usuarios.query.filter_by(email=email).first()
        if not usuario:
            usuario = Usuarios(nombre=nombre, email=email)
            db.session.add(usuario)
            db.session.commit()

        folio = str(uuid.uuid4())  # Generar un folio único

        # Guardar las respuestas
        for pregunta_id in request.form:
            if pregunta_id.startswith('pregunta_'):
                id_pregunta = int(pregunta_id.split('_')[1])
                id_opcion = int(request.form[pregunta_id])  # Obtener la opción seleccionada

                respuesta = Respuestas(
                    id_usuario=usuario.id,
                    id_pregunta=id_pregunta,
                    id_opcion=id_opcion,
                    folio=folio  # Asignar el folio a cada respuesta
                )
                db.session.add(respuesta)

        db.session.commit()

        flash(f'Tu folio de respuestas es: {folio}')
        return redirect(url_for('index'))

    preguntas = Preguntas.query.all()
    opciones = OpcionesRespuesta.query.all()
    return render_template('survey.html', preguntas=preguntas, opciones=opciones)



@app.route('/graficar')
def results():
    # Calculate learning style and generate spider chart
    return render_template('graficar.html', plot_url=generate_spider_chart())

def generate_spider_chart():
    # Calculate results and create spider chart
    return plot_url

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')  # Asegúrate de manejar la contraseña de forma segura

        connection = None
        cursor = None
        
        try:
            # Conectar a la base de datos
            connection = pymysql.connect(
                host='localhost',
                user='root',
                password='G170122fg#',
                database='Cuest'
            )
            cursor = connection.cursor()
            
            # Ejecutar el procedimiento almacenado
            cursor.callproc('insertar_usuario', (nombre, email, contrasena))
            
            # Confirmar los cambios
            connection.commit()

            flash('Usuario registrado exitosamente')
            return redirect(url_for('index'))
        except Exception as e:
            print(f'Error: {e}')
            flash('Error al registrar el usuario')
        finally:
            # Asegúrate de cerrar el cursor y la conexión, si fueron creados
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    return render_template('registro.html')

from werkzeug.security import check_password_hash

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        contrasena = request.form['contrasena']

        usuario = Usuarios.query.filter_by(email=email).first()

        if usuario and check_password_hash(usuario.contrasena, contrasena):
            session['user_id'] = usuario.id
            flash('Inicio de sesión exitoso')
            return redirect(url_for('index'))
        else:
            flash('Correo o contraseña incorrectos.')

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
