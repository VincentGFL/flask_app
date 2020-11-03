from app import db, Countries, Cities

db.drop_all()
db.create_all()

UK = Countries(name='United Kingdom')
db.session.add(UK)
db.session.commit()

london = Cities(name='London', country=UK)
manchester = Cities(name='Manchester', country=Countries.query.filter_by(name='United Kingdom').first())
liverpool = Cities(name='Liverpool', country_id=UK.id)

db.session.add(london)
db.session.add(manchester)
db.session.add(liverpool)
db.session.commit()
