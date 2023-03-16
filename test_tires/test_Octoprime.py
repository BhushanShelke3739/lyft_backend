import unittest

from tires.tires_Octoprime import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        self.v1 = 0.2
        self.v2 = 0.9
        self.v3 = 0.9
        self.v4 = 1
        if  self.v1 + self.v2 +self.v3 + self.v4 >= 3 :
            self.assertTrue(OctoprimeTires.needs_service())

    def test_needs_service_false(self):
        self.v1 = 0
        self.v2 = 0.25
        self.v3 = 0.6
        self.v4 = 0.7
        if  self.v1 + self.v2 +self.v3 + self.v4 <= 3 :
            self.assertFalse(OctoprimeTires.needs_service())