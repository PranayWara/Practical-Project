
from flask import url_for
from flask_testing import TestCase
import requests_mock
import app
from application import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY = "dfs",
            WTF_CSRF_ENABLED = False
        )
        return app

    def setup(self):
        db.create_all()

    def teardown(self):
        db.drop_all()

class TestResponse(TestBase):
    def test_index(self):
        with requests_mock.mock() as m:
            a = self.client.get(url_for('index'))
            self.assert500(a)
            m.get('http://service_2:5002/get/rarity', json='Blue')
            m.get('http://service_3:5003/get/gun', json='Glock-18')
            m.post('http://service_4:5004/post/winnings', json=2)

            response = self.client.get(url_for('index'))

        self.assert500(response)
        self.assertIn('You rolled a Blue Glock-18 worth £2', response.data.decode())
        