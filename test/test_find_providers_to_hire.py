from unittest import TestCase
from find_providers_to_hire import FindProvidersToHireUseCase
from provider import Provider


class TestFindProvidersToHireUseCase(TestCase):

    def test_instance_one(self):
        # given
        use_case = FindProvidersToHireUseCase()
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
        providers_to_hire = use_case.invoke(providers, 1000)

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
        use_case = FindProvidersToHireUseCase()
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
        providers_to_hire = use_case.invoke(providers, 500)

        # then
        self.assertTrue(len(providers_to_hire) == 2)
        self.assertTrue(Provider(radius=100, position=100, provider_id=6)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=200, position=300, provider_id=7)
                        in providers_to_hire)

    def test_instance_three(self):
        # given
        use_case = FindProvidersToHireUseCase()
        providers = [
            Provider(radius=50, position=44, provider_id=1),
            Provider(radius=150, position=402, provider_id=2),
            Provider(radius=35, position=219, provider_id=3),
            Provider(radius=80, position=100, provider_id=4),
            Provider(radius=80, position=80, provider_id=5),
            Provider(radius=160, position=300, provider_id=6),
            Provider(radius=30, position=150, provider_id=7)
        ]

        # when
        providers_to_hire = use_case.invoke(providers, 500)

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
        use_case = FindProvidersToHireUseCase()
        providers = [
            Provider(radius=150, position=50, provider_id=1),
            Provider(radius=100, position=100, provider_id=2),
            Provider(radius=150, position=300, provider_id=3),
            Provider(radius=100, position=200, provider_id=4),
            Provider(radius=275, position=450, provider_id=5),
            Provider(radius=50, position=650, provider_id=6),
            Provider(radius=150, position=850, provider_id=7)
        ]

        # when
        providers_to_hire = use_case.invoke(providers, 1000)

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
        use_case = FindProvidersToHireUseCase()
        providers = [
            Provider(radius=250, position=250, provider_id=1),
            Provider(radius=250, position=750, provider_id=2)
        ]

        # when
        providers_to_hire = use_case.invoke(providers, 1000)

        # then
        self.assertTrue(len(providers_to_hire) == 2)
        self.assertTrue(Provider(radius=250, position=250, provider_id=1)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=250, position=750, provider_id=2)
                        in providers_to_hire)

    def test_instance_six(self):
        # given
        use_case = FindProvidersToHireUseCase()
        providers = [
            Provider(radius=50, position=50, provider_id=1),
            Provider(radius=50, position=100, provider_id=2),
            Provider(radius=40, position=140, provider_id=3),
            Provider(radius=30, position=150, provider_id=4)
        ]

        # when
        providers_to_hire = use_case.invoke(providers, 180)

        # then
        self.assertTrue(len(providers_to_hire) == 2)
        self.assertTrue(Provider(radius=50, position=50, provider_id=1)
                        in providers_to_hire)
        self.assertTrue(Provider(radius=40, position=140, provider_id=3)
                        in providers_to_hire)
