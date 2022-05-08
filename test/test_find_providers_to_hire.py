from unittest import TestCase

from src.model.provider import Provider
from src.model.provider_service import SolutionNotFound, ProviderService
from src.use_case.find_providers_to_hire import find_providers_to_hire
from test.providers_factory import instance_one, instance_three, instance_two, instance_four

service = ProviderService()


class TestFindProvidersToHireUseCase(TestCase):

    def test_instance_one(self):
        # given
        providers = instance_one()

        # when
        providers_to_hire = find_providers_to_hire(providers, 1000)

        # then
        self.assertTrue(len(providers_to_hire) == 4)
        self.assertTrue(Provider(radius=100, position=100, provider_id=6)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=200, position=300, provider_id=7)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=220, position=680, provider_id=9)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=250, position=980, provider_id=1)
                        in providers_to_hire)

    def test_instance_two(self):
        # given
        providers = instance_two()

        # when
        providers_to_hire = find_providers_to_hire(providers, 500)

        # then
        self.assertTrue(len(providers_to_hire) == 2)
        self.assertTrue(Provider(radius=100, position=100, provider_id=6)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=200, position=300, provider_id=7)
                        in providers_to_hire)

    def test_instance_three(self):
        # given
        providers = instance_three()

        # when
        providers_to_hire = find_providers_to_hire(providers, 500)

        # then
        self.assertTrue(len(providers_to_hire) == 3)
        self.assertTrue(Provider(radius=80, position=80, provider_id=5)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=160, position=300, provider_id=6)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=150, position=402, provider_id=2)
                        in providers_to_hire)

    def test_instance_four(self):
        # given
        providers = instance_four()

        # when
        providers_to_hire = find_providers_to_hire(providers, 1000)

        # then
        self.assertTrue(len(providers_to_hire) == 3)
        self.assertTrue(Provider(radius=100, position=100, provider_id=2)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=275, position=450, provider_id=5)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=150, position=850, provider_id=7)
                        in providers_to_hire)

    def test_instance_five(self):
        # given
        providers = [
            Provider(radius=250, position=250, provider_id=1),
            Provider(radius=250, position=750, provider_id=2)
        ]
        providers = service.sort(providers)

        # when
        providers_to_hire = find_providers_to_hire(providers, 1000)

        # then
        self.assertTrue(len(providers_to_hire) == 2)
        self.assertTrue(Provider(radius=250, position=250, provider_id=1)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=250, position=750, provider_id=2)
                        in providers_to_hire)

    def test_instance_six(self):
        # given
        providers = [
            Provider(radius=50, position=50, provider_id=1),
            Provider(radius=50, position=100, provider_id=2),
            Provider(radius=40, position=140, provider_id=3),
            Provider(radius=30, position=150, provider_id=4)
        ]
        providers = service.sort(providers)

        # when
        providers_to_hire = find_providers_to_hire(providers, 180)

        # then
        self.assertTrue(len(providers_to_hire) == 2)
        self.assertTrue(Provider(radius=50, position=50, provider_id=1)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=40, position=140, provider_id=3)
                        in providers_to_hire)

    def test_instance_without_a_solution_must_throw_an_error(self):
        with self.assertRaises(SolutionNotFound):
            # given
            providers = [
                Provider(radius=50, position=50, provider_id=1),
                Provider(radius=50, position=100, provider_id=2),
                Provider(radius=40, position=140, provider_id=3),
                Provider(radius=30, position=150, provider_id=4)
            ]
            providers = service.sort(providers)

            # when
            find_providers_to_hire(providers, 1000)

    def test_instance_without_a_complete_coverage_offer_must_throw_an_error(self):
        with self.assertRaises(SolutionNotFound):
            # given
            providers = [
                Provider(radius=50, position=50, provider_id=1),
                Provider(radius=50, position=120, provider_id=2),
                Provider(radius=20, position=210, provider_id=3),
                Provider(radius=40, position=250, provider_id=4)
            ]
            providers = service.sort(providers)

            # when
            find_providers_to_hire(providers, 250)
