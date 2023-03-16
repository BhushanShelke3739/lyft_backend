import unittest

from tires.tires_Carrigan import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        self.v1 = 0
        self.v2 = 0.25
        self.v3 = 0.6
        self.v4 = 1
        self.assertTrue(CarriganTires.needs_service())

    def test_needs_service_false(self):
        self.v1 = 0
        self.v2 = 0.25
        self.v3 = 0.6
        self.v4 = 0.7
        self.assertFalse(CarriganTires.needs_service())