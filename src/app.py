from flask import Flask, render_template, url_for, request, redirect
from config import *
from persona import Persona

con_db = conection()

app = Flask(__name__)

#ruta de la pagina principal
@app.route("/")
def index():
    return render_template("index.html")

#guardar los usuarios
@app.route("/guardar_user", methods=['POST'])
def guardar_user():
    users = con_db['usuario'] #crea la coleccion usuarios
    name = request.form['name']
    apellido = request.form['apellido']
    email = request.form['email']
    password = request.form['password']
    print(name, apellido, email, password)
    if name != '' and apellido != '' and email != '' and password != '':
        user = Persona(name, apellido, email, password)
        users.insert_one(user.formato_doc()) #inserta los datos en la coleccion usuarios
        return redirect(url_for('index'))
    else:
        return render_template("error.html")


#ruta de error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
	app.run(debug=True, port=5000)
