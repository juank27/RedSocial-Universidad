class Persona:
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def formato_doc(self):
        return {
            'name': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'password': self.password
        }
