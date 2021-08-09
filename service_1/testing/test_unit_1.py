
from flask import url_for
from flask_testing import TestCase
import requests_mock

from app import app, db

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///"
        )
        return app

    def setup(self):
        db.create_all()

    def teardown(self):
        db.drop_all()

class TestResponse(TestBase):
    def test_index(self):
        with requests_mock.mock() as m:
            m.get('http://service_2:5002/get/rarity', json='Blue')
            m.get('http://service_3:5003/get/gun', json='AK-47')
            m.post('http://service_4:5004/post/winnings', json=6)

            response = self.client.get(url_for('index'))

        self.assert500(response)
        self.assertIn('You rolled a Blue AK-47 worth £6', response.data.decode())
        