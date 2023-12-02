from flask import Flask
import sys
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Mundo! cambio'

@app.route('/romper')
def romper():
    os._exit(1)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
