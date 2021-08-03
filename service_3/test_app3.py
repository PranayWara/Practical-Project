import pytest
from flask import  app, url_for 
from flask_testing import TestCase
from sqlalchemy import desc
from app import app

class testbase(TestCase):
    def create_app(self):
        return app


class TestViews(testbase):

    def test_gun_get(self):
        response = self.client.get(url_for('gun'))
        self.assertEqual(response.status_code, 200)