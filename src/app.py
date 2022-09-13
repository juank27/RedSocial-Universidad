from flask import Flask, render_template, url_for, request, redirect
from config import *
from persona import Persona
from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funciona

con_db = conection()

app = Flask(__name__)

#ruta de la pagina principal
@app.route("/")
def index():
    return render_template("indexPrueba.html")

#ruta de la pagina principal
@app.route("/update_user")
def update_user():
    users = con_db['usuario']
    encontrados = users.find()
    print(encontrados)
    return render_template("update_user.html", users=encontrados)

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

#eliminar usuarios
@app.route("/delete/<_id>")
def delete(_id):
    print("🚀 ~ file: app.py ~ line 41 ~ name", _id)
    print(type(_id))
    users = con_db['usuario']
    # users.delete_one({"name": name})
    users.delete_one({"_id": ObjectId(_id) })
    return redirect(url_for('update_user'))

#update usuarios
@app.route("/update/<string:namee>", methods=['POST'])
def update(namee):
    users = con_db['usuario']
    name = request.form['name']
    apellido = request.form['apellido']
    email = request.form['email']
    password = request.form['password']
    # user = users.find_one({"name": name})
    print(name, apellido, email, password)
    if name != '' and apellido != '' and email != '' and password != '':
        users.update_one({"name": namee},
        {
            "$set": {
                    "name": name,
                    "apellido": apellido,
                    "email": email,
                    "password": password
                }
        })
        return redirect(url_for('update_user'))
    else:
        return redirect(url_for('page_not_found'))


@app.route("/yadir")
def yadir():
    return render_template("yadir.html")

@app.route("/emerson")
def emerson():
    return render_template("emerson.html")

@app.route("/andres")
def andres():
    return render_template("andres.html")

@app.route("/karen")
def karen():
    return render_template("karen.html")

@app.route("/juan")
def juan():
    return render_template("juan.html")

#ruta de error 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
	app.run(debug=True, port=5000)
