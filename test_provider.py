from unittest import TestCase

from provider import Provider


class TestProvider(TestCase):

    def test_lower_position_must_be_ok(self):
        # given
        radius = 250
        position = 980
        provider = Provider(radius=radius, position=position, provider_id=1)
        expected_position = radius + position

        # then
        self.assertEqual(expected_position, provider.lower_position())

    def test_higher_position_must_be_ok(self):
        # given
        provider = Provider(radius=250, position=980, provider_id=1)

        # then
        self.assertEqual(1230, provider.higher_position())
