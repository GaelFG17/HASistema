import matplotlib
matplotlib.use('Agg')  # Este backend es adecuado para generar gráficos en servidores sin GUI
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import io
import base64
import pandas as pd
import numpy as np
import uuid
from werkzeug.security import generate_password_hash, check_password_hash

# Configuración de la aplicación
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql123@localhost/Encuestas'
db = SQLAlchemy(app)

# Definición de los modelos de base de datos
class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contrasena = db.Column(db.String(200), nullable=False)
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
    folio = db.Column(db.String(100), nullable=False)

# Rutas de la aplicación
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')

        usuario = Usuarios.query.filter_by(email=email).first()
        if not usuario:
            usuario = Usuarios(nombre=nombre, email=email)
            db.session.add(usuario)
            db.session.commit()

        folio = str(uuid.uuid4())

        for pregunta_id in request.form:
            if pregunta_id.startswith('pregunta_'):
                id_pregunta = int(pregunta_id.split('_')[1])
                id_opcion = int(request.form[pregunta_id])

                respuesta = Respuestas(
                    id_usuario=usuario.id,
                    id_pregunta=id_pregunta,
                    id_opcion=id_opcion,
                    folio=folio
                )
                db.session.add(respuesta)

        db.session.commit()

        flash(f'Tu folio de respuestas es: {folio}')
        return redirect(url_for('index'))

    preguntas = Preguntas.query.all()
    opciones = OpcionesRespuesta.query.all()
    return render_template('survey.html', preguntas=preguntas, opciones=opciones)

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('contrasena')

    usuario = Usuarios.query.filter_by(email=email).first()

    if usuario and check_password_hash(usuario.contrasena, password):
        session['user_id'] = usuario.id
        flash('Inicio de sesión exitoso')
        return redirect(url_for('menu'))
    else:
        flash('Correo o contraseña incorrectos')
        return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')

        contrasena_hash = generate_password_hash(contrasena, method='pbkdf2:sha256')

        nuevo_usuario = Usuarios(nombre=nombre, email=email, contrasena=contrasena_hash)
        db.session.add(nuevo_usuario)
        db.session.commit()

        flash('Registro exitoso, ahora puedes iniciar sesión')
        return redirect(url_for('index'))

    return render_template('registrar.html')

def generate_spider_chart(categorias_respuestas):
    labels = list(categorias_respuestas.keys())
    values = list(categorias_respuestas.values())

    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='red', alpha=0.25)
    ax.plot(angles, values, color='red', linewidth=2)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    plt.close(fig)

    return f"data:image/png;base64,{img_base64}"

@app.route('/graficar')
def results():
    user_id = session.get('user_id')
    if user_id is None:
        flash('Debes iniciar sesión para ver esta página')
        return redirect(url_for('index'))

    respuestas = Respuestas.query.filter_by(id_usuario=user_id).all()

    pregunta_ids = set(respuesta.id_pregunta for respuesta in respuestas)
    categorias = Preguntas.query.filter(Preguntas.id.in_(pregunta_ids)).all()
    
    categorias_respuestas = {categoria: 0 for categoria in ['Activo', 'Reflexivo', 'Teórico', 'Pragmático']}
    
    for respuesta in respuestas:
        pregunta = db.session.get(Preguntas, respuesta.id_pregunta)
        categorias_respuestas[pregunta.categoria] += 1

    plot_url = generate_spider_chart(categorias_respuestas) 
    return render_template('resul.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
