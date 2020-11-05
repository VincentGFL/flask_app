import unittest
from flask import url_for
from flask_testing import TestCase

from app import app, db, Register

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='SECRET',
                DEBUG=True)
        return app

    def setUp(self):
        db.create_all()

        sample = Register(name="MissWoman")

        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code, 405)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code, 405)

class TestUpdate(TestBade):
    def test_update_post(self):
        response = self.client.post(url_for("update"),
            data = dict(oldname="MissWoman", newname="MissLady"),
            follow_redirects=True
            )
        self.assertEqual(response.status_code, 200)

class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(url_for("Update"),
            data = dict(oldname="MissWoman", newname="missLady"),
            follow_redirects=True
            )
        self.assertEqua(response.status_code, 200)

