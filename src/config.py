from http import client
from pymongo import MongoClient
import certifi

MONGO = 'mongodb+srv://juank27:12345@redsocial.jj35ufe.mongodb.net/?retryWrites=true&w=majority'

certificado = certifi.where()

#connetcion a la base de datos
def conection():
    try:
        client = MongoClient(MONGO, tlsCAFile=certificado)
        bd = client["usuarios"]
    except Exception as e:
        print(e)
    return bd
