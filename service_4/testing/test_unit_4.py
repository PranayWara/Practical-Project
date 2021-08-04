from flask import url_for
from flask_testing import TestCase

from service_4.app import app, post_winnings

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_rarity(self):

        for rarity in post_winnings['rarity']:
            for gun in post_winnings['gun']:

                payload = {'rarity':rarity, 'gun':gun}
                response = self.client.post(url_for('post_winnings'), json=payload)

                self.assert200(response)

                expected_price = round(post_winnings['rarity'][rarity] + post_winnings['gun'][gun])
                self.assertEqual(response.json, expected_price)