from flask import render_template, redirect, url_for, request
from application import app, db
from application.models import Todo
from application.forms import TodoForm, OrderForm

@app.route('/', methods=['GET','POST'])
def index():
    form = OrderForm()
    totals = {
            'number_completed':Todo.query.filter_by(completed=True).count(),
            'total':Todo.query.count()
            }


    form = OrderForm()
    if form.order.data == 'new':
        all_todo = Todo.query.order_by(Todo.id.desc()).all()
    elif form.order.data == 'old':
        all_todo = Todo.query.order_by(Todo.id).all()
    elif form.order.data== 'completed':
        all_todo = Todo.query.order_by(Todo.completed.desc()).all()
    elif form.order.data == 'incompleted':
        all_todo = Todo.query.order_by(Todo.completed).all()
    else:
        all_todo = Todo.query.all()
    
    return render_template('index.html', all_todo=all_todo, form=form)

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

