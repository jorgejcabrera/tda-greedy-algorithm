import unittest

from src.model.provider_reader import ProviderReader
from src.model.provider_service import SolutionNotFound
from src.use_case.find_providers_to_hire import find_providers_to_hire


class TestIntegration(unittest.TestCase):

    def test_reading_contratos_2_file_without_any_solution_must_throw_an_error(self):
        with self.assertRaises(SolutionNotFound):
            # given
            reader = ProviderReader("../files/contratos_2.txt")
            providers = reader.read()

            # when
            find_providers_to_hire(providers, int(100))

    def test_reading_contratos_3_file_without_any_solution_must_throw_an_error(self):
        with self.assertRaises(SolutionNotFound):
            # given
            reader = ProviderReader("../files/contratos_3.txt")
            providers = reader.read()

            # when
            find_providers_to_hire(providers, int(110))

    def test_reading_contratos_1_file_with_a_solution_must_not_throw_an_error(self):
        # given
        reader = ProviderReader("../files/contratos_1.txt")
        providers = reader.read()

        # when
        providers = find_providers_to_hire(providers, int(110))

        # then
        self.assertTrue(1 == len(providers))

    def test_reading_contratos_4_file_with_a_solution_must_not_include_unnecessary_providers(self):
        # given
        reader = ProviderReader("../files/contratos_4.txt")
        providers = reader.read()

        # when
        providers = find_providers_to_hire(providers, int(225))

        # then
        self.assertTrue(2 == len(providers))

    def test_reading_contratos_5_file_with_a_solution_must_not_include_unnecessary_providers(self):
        # given
        reader = ProviderReader("../files/contratos_5.txt")
        providers = reader.read()

        # when
        providers = find_providers_to_hire(providers, int(275))

        # then
        self.assertTrue(2 == len(providers))

    def test_reading_contratos_6_file_with_a_solution_must_not_include_unnecessary_providers(self):
        # given
        reader = ProviderReader("../files/contratos_6.txt")
        providers = reader.read()

        # when
        providers = find_providers_to_hire(providers, int(275))

        # then
        self.assertTrue(2 == len(providers))

    def test_reading_contratos_7_without_a_solution_must_throw_an_error(self):
        with self.assertRaises(SolutionNotFound):
            # given
            reader = ProviderReader("../files/contratos_7.txt")
            providers = reader.read()

            # when
            find_providers_to_hire(providers, int(400))

    def test_reading_contratos_8_file_with_a_solution_must_not_include_unnecessary_providers(self):
        # given
        reader = ProviderReader("../files/contratos_8.txt")
        providers = reader.read()

        # when
        providers = find_providers_to_hire(providers, int(400))

        # then
        self.assertTrue(4 == len(providers))
