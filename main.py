'''
modulo principal do meu projeto flask
data: 27/03/2025
autor: victor duarte
'''

from flask import Flask

app = Flask(__name__)
app.secret_key = 'm1_s3cret'

from views import *

if __name__ == '__main__':
    app.run(debug=True)