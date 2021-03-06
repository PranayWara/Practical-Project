from flask import  app, url_for 
from flask_testing import TestCase
from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


class TestViews(TestBase):
    def test_rarity_get(self):
        response = self.client.get(url_for('rarity'))
        self.assertEqual(response.status_code, 200)