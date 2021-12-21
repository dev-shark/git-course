#def sum (a,b):
#    return a+b
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hola mundo"
@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    suma = a+b
    return f"La suma es: {str(suma)}"
#app * Flask(__name__)
