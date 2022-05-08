import unittest

from find_providers_to_hire import FindProvidersToHireUseCase
from provider_reader import ProviderReader
from provider_service import SolutionNotFound


class TestIntegration(unittest.TestCase):

    def test_reading_contratos_2_file_without_any_solution_must_throw_an_error(self):
        with self.assertRaises(SolutionNotFound):
            # given
            reader = ProviderReader("../files/contratos_2.txt")
            providers = reader.read()
            use_case = FindProvidersToHireUseCase()

            # when
            use_case.invoke(providers, int(100))

    def test_reading_contratos_3_file_without_any_solution_must_throw_an_error(self):
        with self.assertRaises(SolutionNotFound):
            # given
            reader = ProviderReader("../files/contratos_3.txt")
            providers = reader.read()
            use_case = FindProvidersToHireUseCase()

            # when
            use_case.invoke(providers, int(110))

    def test_reading_contratos_1_file_with_a_solution_must_not_throw_an_error(self):
        # given
        reader = ProviderReader("../files/contratos_1.txt")
        providers = reader.read()
        use_case = FindProvidersToHireUseCase()

        # when
        providers = use_case.invoke(providers, int(110))

        # then
        self.assertTrue(1 == len(providers))
