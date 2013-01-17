from problems.spaceship_purchase import checkio
from test.testgen import test_generator

__author__ = 'dikei'

import unittest


class SpaceshipPurchaseTest(unittest.TestCase):
    pass

def gen_test():
    cases = (
        (450, [150, 50, 1000, 100]),
        (700, [500, 300, 700, 100])
    )
    for index, case in enumerate(cases):
        test_name = "test_spaceship_purchase_{}".format(index)
        test_func = test_generator(case[0], case[1], checkio)
        setattr(SpaceshipPurchaseTest, test_name, test_func)