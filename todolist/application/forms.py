from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, ValidationError
from application.models import Todo


class TodoCheck:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        all_todos = Todo.query.all()
        for todo in all_todos:
            if todo.name == field.data:
                raise ValidationError(self.message)

class Sort(FlaskForm):
    sort = QuerySelectField("Completed first", Todo.query.order_by(Todo.completed).all())

class TodoForm(FlaskForm):
    task = StringField('Task', validators=[DataRequired(), 
        TodoCheck(message='Task name already exist')])
    submit = SubmitField('Add Task')


