from unittest import TestCase

from provider import Provider


class TestProvider(TestCase):

    def test_lower_position_must_be_ok(self):
        # given
        radius = 250
        position = 980
        provider = Provider(radius=radius, position=position, provider_id=1)
        expected_position = position - radius

        # then
        self.assertEqual(expected_position, provider.lower_position())

    def test_higher_position_must_be_ok(self):
        # given
        radius = 250
        position = 980
        expected_position = radius + position

        provider = Provider(radius=250, position=980, provider_id=1)

        # then
        self.assertEqual(expected_position, provider.higher_position())
