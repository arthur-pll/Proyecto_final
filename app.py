from flask import Flask, render_template, request
import os
import matplotlib.pyplot as plt
import random
import time


app = Flask(__name__)#freamwore de desarrollo

@app.route('/')
def inicio():
    return render_template('main.html')

@app.route('/inicio')
def inicio_user():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html', title='Registro de usuarios')

@app.route('/crearUsuario', methods=['POST'])
def crearUsuario():
    if request.method == "POST":
        usuario = request.form['usuario']
        pwd= request.form['pwd']

        with open('proyecto final/static/usuarios.csv','a') as f:
            f.write(usuario+";"+pwd+"\n")

        return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        usuario = request.form['usuario']
        password= request.form['password']

        directorio=os.path.dirname(__file__)
        archivo = 'static/usuarios.csv'
        ruta = os.path.join(directorio,archivo) 
        with open(ruta,'r') as f:
            datos = f.readlines()
            
        encontrado = False
        for usuarioFile in datos:
            datosUsuario = usuarioFile.replace("\n","").split(";")
            if (usuario == datosUsuario[0] and password == datosUsuario[1]):
                encontrado = True
                crearGrafica()
                return render_template('Menu.html',usuario=usuario)
            
        if encontrado == False:
            return "Datos inválidos"

def crearGrafica():
    x = []  
    y = []
    for i in range(20):
        dato = random.randint(80, 160)
        x.append(time.time()) 
        y.append(dato) 
        plt.plot(x, y, color='blue')
        plt.title('Gluco Rate Monitor')  
        plt.xlabel('Tiempo')  
        plt.ylabel('Muestra')  
        time.sleep(0.1)
    directorio = os.path.dirname(__file__)
    archivo = 'static/grafica.png'
    ruta = os.path.join(directorio,archivo)
    plt.title('Gluco Rate Monitor')  
    plt.xlabel('Tiempo') 
    plt.ylabel('Muestra')  
    plt.savefig(ruta, bbox_inches='tight')
    return ""

@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    peso = request.form['peso']

    resultado = {
        'nombre': nombre,
        'email': email,
        'telefono': telefono,
        'peso': peso
    }
    return render_template('menu.html', resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)