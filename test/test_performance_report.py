import time
from unittest import TestCase

import matplotlib.pyplot as plt

from src.use_case.find_providers_to_hire import FindProvidersToHireUseCase
from test.providers_factory import sample_of


def current_milli_time():
    return round(time.time() * 1000)


class TestPerformanceReport(TestCase):

    def test_measure_of_greedy_v1_implementation(self):
        find_providers_to_hire = FindProvidersToHireUseCase()
        amount_of_providers = 10
        kilometers = 20000
        x = []
        y_v2 = []
        while amount_of_providers < kilometers:
            providers = sample_of(amount_of_providers, kilometers)

            started_time_v2 = current_milli_time()
            find_providers_to_hire.invoke(providers, kilometers)
            end_time_v2 = current_milli_time() - started_time_v2

            x.append(amount_of_providers)
            y_v2.append(end_time_v2)

            amount_of_providers += 500

        plt.plot(x, y_v2, label="v2")
        plt.legend(loc='upper center')

        # naming the x axis
        plt.xlabel('Providers')
        # naming the y axis
        plt.ylabel('Total time (ms)')

        # giving a title to my graph
        plt.title('Strategy Performance')

        plt.show()

        self.assertTrue(1 == 1)
