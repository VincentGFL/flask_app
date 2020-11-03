from application import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    completed = db.Column(db.Boolean, default=False)
