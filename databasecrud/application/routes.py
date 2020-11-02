from application import app, db
from application.models import Games

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>" +game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/delete/<int:id>')
def delete(id):
    game_to_delete = Games.query.get(id)#or Games.query.filter_by(id=id).first()
    db.session.delete(game_to_delete)
    db.session.commit()
    return game_to_delete.name + " has been deleted"

@app.route('/count')
def count():
    number_of_games = Games.query.count()
    return str(number_of_games)
