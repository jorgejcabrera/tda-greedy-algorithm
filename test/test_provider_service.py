from unittest import TestCase

from src.model.provider import Provider
from src.model.provider_service import ProviderService
from test.providers_factory import instance_one, instance_two


class TestProviderService(TestCase):

    def test_the_best_provider_must_reach_the_highest_position(self):
        # given
        service = ProviderService()
        providers = instance_one()

        # when
        best_provider = service.find_the_best_of(providers)

        # then
        self.assertEqual(1230, best_provider.higher_position())

    def test_when_subtract_providers_then_all_of_those_must_not_be_anymore(self):
        # given
        service = ProviderService()
        providers = instance_one()
        providers_to_subtract = instance_two()

        # when
        providers = service.subtract(providers, providers_to_subtract)

        # then
        self.assertEqual(2, len(providers))
        self.assertTrue(Provider(radius=250, position=980, provider_id=1) in providers)
        self.assertTrue(Provider(radius=150, position=50, provider_id=10) in providers)

    def test_when_sort_providers_then_they_must_be_sorted_by_lower_position(self):
        # given
        service = ProviderService()
        providers = instance_one()

        # when
        sorted_providers = service.sort(providers)

        # then
        self.assertTrue(10, sorted_providers[0].id)
        self.assertTrue(6, sorted_providers[1].id)
        self.assertTrue(7, sorted_providers[2].id)
        self.assertTrue(5, sorted_providers[3].id)
        self.assertTrue(8, sorted_providers[4].id)
        self.assertTrue(2, sorted_providers[5].id)
        self.assertTrue(3, sorted_providers[6].id)
        self.assertTrue(9, sorted_providers[7].id)
        self.assertTrue(4, sorted_providers[8].id)
        self.assertTrue(1, sorted_providers[9].id)

    def test_when_find_providers_with_coverage_below_position_then_all_with_a_lower_position_smaller_must_be_retrieved(
            self):
        # given
        service = ProviderService()
        providers = instance_one()
        providers = service.sort(providers)

        # when
        filtered_providers = service.find_all_with_coverage_below(providers, 200)

        # then
        self.assertTrue(len(filtered_providers) == 4)
        self.assertTrue(Provider(radius=150, position=50, provider_id=10) in providers)
        self.assertTrue(Provider(radius=100, position=100, provider_id=6) in providers)
        self.assertTrue(Provider(radius=200, position=300, provider_id=7) in providers)
        self.assertTrue(Provider(radius=80, position=270, provider_id=5) in providers)
