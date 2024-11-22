"""
Shichao Tian
Final project Models Class Graffiti
"""
import unittest
from models.graffiti import Graffiti


class TestGraffiti(unittest.TestCase):
    def setUp(self):
        self.graffitis = [
            Graffiti(10, "Midtown", (40.785091, -73.968285)),
            Graffiti(5, "Brooklyn", (40.660204, -73.968956)),
            Graffiti(0, "Ghost Town", (0.0, 0.0))]

    def test_graffiti_in_neighbour(self):
        result = Graffiti.graffiti_in_neighbour(self.graffitis)
        expected = {'Midtown': 10, 'Brooklyn': 5, 'Ghost Town': 0}
        self.assertEqual(result, expected)

    def test_graffiti_in_neighbour_empty(self):
        self.assertEqual(Graffiti.graffiti_in_neighbour([]), {})


if __name__ == '__main__':
    unittest.main()
