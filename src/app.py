#def sum (a,b):
#    return a+b
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hola mundo"

#app * Flask(__name__)
