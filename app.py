'''
modulo principal do meu projeto flask
data: 27/03/2025
autor: victor duarte
'''

from flask import Flask
from tasks.routes import task
from tasks.database import db

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)

app.register_blueprint(task)

with app.app_context():
    db.create_all()    


if __name__ == '__main__':
    app.run(debug=True)