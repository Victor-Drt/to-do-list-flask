from flask import render_template, request, redirect, url_for
from models.task import Task
from main import app


tasks = []

@app.route('/')
def index():
    '''
    rota de inicio
    '''
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST',])
def create():
    name = request.form['title']
    nova_task = Task(name, False)
    tasks.append(nova_task)
    
    return redirect(url_for('index'))

@app.route('/check/<string:title>')
def check(title):
    for task in tasks:
        if task.title == title:
            task.status = not task.status
    return redirect(url_for('index'))

@app.route('/deletar/<string:title>')
def delete(title):
    task_deletada = None

    for task in tasks:
        if task.title == title:
            task_deletada = task

    tasks.remove(task_deletada)

    return redirect(url_for('index'))
