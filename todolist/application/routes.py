from flask import render_template, redirect, url_for
from application import app, db
from application.models import Todo

@app.route('/')
def index():
    all_todo = Todo.query.all()
    return render_template('index.html', all_todo=all_todo)

@app.route('/add')
def add():
    new_todo = Todo(name="New To Do Task")
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/completed/<int:todo_id>')
def completed(todo_id):
    todo_to_update = Todo.query.get(todo_id)
    todo_to_update.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incompleted/<int:todo_id>')
def incompleted(todo_id):
    todo_to_update = Todo.query.get(todo_id)
    todo_to_update.completed = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<name>')
def update(name):
    todo_to_update = Todo.query.first()
    todo_to_update.name = name
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete')
def delete():
    todo_to_delete = Todo.query.first()
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

