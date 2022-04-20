from unittest import TestCase

import matplotlib.pyplot as plt

import time


def current_milli_time():
    return round(time.time() * 1000)


class TestPerformanceOfRankingCreation(TestCase):

    def test_measure_of_greedy_v1_implementation(self):
        self.assertTrue(1 == 1)
