from unittest import TestCase

import matplotlib.pyplot as plt

import time

from find_providers_to_hire import FindProvidersToHireUseCase
from test.providers_factory import sample_of


def current_milli_time():
    return round(time.time() * 1000)


class TestPerformanceReport(TestCase):

    def test_measure_of_greedy_v1_implementation(self):
        find_providers_to_hire = FindProvidersToHireUseCase()
        amount_of_providers = 10
        kilometers = 100000
        x = []
        y = []
        while amount_of_providers < kilometers:
            providers = sample_of(amount_of_providers, kilometers)
            started_time = current_milli_time()
            find_providers_to_hire.invoke_v1(providers, kilometers)
            end_time = current_milli_time() - started_time

            x.append(amount_of_providers)
            y.append(end_time)

            amount_of_providers += 500

        plt.plot(x, y)
        # function to show the plot
        plt.show()
        self.assertTrue(1 == 1)
