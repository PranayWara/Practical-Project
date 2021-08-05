
from flask import url_for
from flask_testing import TestCase
from requests_mock import mock

from service_1.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_index(self):

        with mock() as m:
            m.get('http://service_2:5000/get/rarity', text='Blue')
            m.get('http://service_3:5000/get/gun', text='AK-47')
            m.post('http://service_4:5000/post/winnings', json=6)

            response = self.client.get(url_for('main'))

        self.assert200(response)
        self.assertIn('You rolled a Blue AK-47 worth £6.00.', response.data.decode())
        