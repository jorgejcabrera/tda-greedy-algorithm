from unittest import TestCase

from provider import Provider
from provider_service import ProviderService


class TestProviderService(TestCase):

    def test_the_best_provider_must_reach_the_highest_position(self):
        # given
        service = ProviderService()
        providers = [
            Provider(radius=250, position=980, provider_id=1),
            Provider(radius=100, position=500, provider_id=2),
            Provider(radius=150, position=600, provider_id=3),
            Provider(radius=300, position=850, provider_id=4),
            Provider(radius=80, position=270, provider_id=5),
            Provider(radius=100, position=100, provider_id=6),
            Provider(radius=200, position=300, provider_id=7),
            Provider(radius=120, position=400, provider_id=8),
            Provider(radius=220, position=680, provider_id=9),
            Provider(radius=150, position=50, provider_id=10)
        ]

        # when
        best_provider = service.find_best_of(providers)

        # then
        self.assertEqual(1230, best_provider.higher_position())

    def test_when_remove_a_subset_of_providers_then_all_of_those_must_be_deleted(self):
        # given
        service = ProviderService()
        providers = [
            Provider(radius=250, position=980, provider_id=1),
            Provider(radius=100, position=500, provider_id=2),
            Provider(radius=150, position=600, provider_id=3),
            Provider(radius=300, position=850, provider_id=4),
            Provider(radius=80, position=270, provider_id=5),
            Provider(radius=100, position=100, provider_id=6),
            Provider(radius=200, position=300, provider_id=7),
            Provider(radius=120, position=400, provider_id=8),
            Provider(radius=220, position=680, provider_id=9),
            Provider(radius=150, position=50, provider_id=10)
        ]
        providers_to_subtract = [
            Provider(radius=100, position=500, provider_id=2),
            Provider(radius=150, position=600, provider_id=3),
            Provider(radius=300, position=850, provider_id=4),
            Provider(radius=80, position=270, provider_id=5),
            Provider(radius=100, position=100, provider_id=6),
            Provider(radius=200, position=300, provider_id=7),
            Provider(radius=120, position=400, provider_id=8),
            Provider(radius=220, position=680, provider_id=9)
        ]

        # when
        providers = service.subtract(providers, providers_to_subtract)

        # then
        self.assertEqual(2, len(providers))
        self.assertTrue(Provider(radius=250, position=980, provider_id=1) in providers)
        self.assertTrue(Provider(radius=150, position=50, provider_id=10) in providers)
