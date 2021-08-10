
from flask import url_for
from flask_testing import TestCase
from requests_mock import mock
from app import app, db
from application.models import history

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY = "dfs",
            WTF_CSRF_ENABLED = False
        )
        return app

    def setUp(self):
        db.create_all()
        test = history(rarity='Pink', gun = 'AWP', price = 9)
        db.session.add(test)
        db.session.commit()


    def tearDown(self):
        db.drop_all()

class TestResponse(TestBase):
    def test_index(self):
        with mock() as m:
            # a = self.client.get(url_for('index'))
            # self.assert500(a)
            m.get('http://service_2:5002/get/rarity', json='Blue')
            m.get('http://service_3:5003/get/gun', json='Glock-18')
            m.post('http://service_4:5004/post/winnings', json=2)

            response = self.client.get(url_for('index'))

        self.assert200(response)
        self.assertIn('You rolled a Blue Glock-18 worth £2', response.data.decode())
        