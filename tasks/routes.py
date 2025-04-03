from flask import render_template, request, redirect, url_for, Blueprint
from tasks.task import Task
from tasks import tasks
from tasks.database import db

task = Blueprint('task', __name__)

@task.route('/')
def index():
    '''
    rota de inicio
    '''
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@task.route('/create', methods=['POST',])
def create():
    nova_task = Task(title=request.form['title'], status=False)
    db.session.add(nova_task)
    db.session.commit()
    
    return redirect(url_for('task.index'))

@task.route('/check/<int:id>')
def check(id):
    task_checked = Task.query.filter_by(id=id).first()
    last_status = task_checked.status
    task_checked.status = not last_status
    
    db.session.add(task_checked)
    db.session.commit()
    
    return redirect(url_for('task.index'))

@task.route('/deletar/<int:id>')
def delete(id):
    
    Task.query.filter_by(id=id).delete()
    db.session.commit()

    return redirect(url_for('task.index'))
