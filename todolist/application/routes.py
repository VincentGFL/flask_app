from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Todo
from application.forms import TodoForm

@app.route('/')
def index():
    all_todo = Todo.query.all()
    return render_template('index.html', all_todo=all_todo)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TodoForm()
    if form.validate_on_submit():
        new_todo = Todo(name=form.task.data)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

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

@app.route('/update/<int:todo_id>', methods=["GET", "POST"])
def update(todo_id):
    form = TodoForm()
    todo_to_update = Todo.query.get(todo_id)
    if form.validate_on_submit():
        todo_to_update.name = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', form=form)

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo_to_delete = Todo.query.get(todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

