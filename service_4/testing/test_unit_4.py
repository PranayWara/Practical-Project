from flask import url_for
from flask_testing import TestCase

from app import app, sp

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_rarity(self):

        for rarity in sp['rarity']:
            for gun in sp['gun']:

                payload = {'rarity':rarity, 'gun':gun}
                response = self.client.post(url_for('price'), json=payload)

                self.assert200(response)

                expected_price = round(sp['rarity'][rarity] + sp['gun'][gun])
                self.assertEqual(response.json, expected_price)