from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=True)
    cities = db.relationship('Cities', backref='country')

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
