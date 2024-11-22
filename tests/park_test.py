"""
Shichao Tian
Final project Model class Park
"""
import unittest
from models.park import Park
from models.graffiti import Graffiti


class TestPark(unittest.TestCase):
    def setUp(self):
        self.parks = [
            Park("Central Park", "Midtown", (40.785091, -73.968285)),
            Park("Prospect Park", "Brooklyn", (40.660204, -73.968956)),
            Park("Riverside Park", "Midtown", (40.796431, -73.970184)),
            Park("Empty Park", "Nowhere", (0.0, 0.0))]

    def test_empty_park_list(self):
        self.assertEqual(Park.park_in_neighbour([]), {})

    def test_park_in_neighbour(self):
        result = Park.park_in_neighbour(self.parks)
        expected = {'Midtown': 2, 'Brooklyn': 1, 'Nowhere': 1}
        self.assertEqual(result, expected)

    def test_graffitis_within_km(self):
        graffiti_instances = [
            Graffiti(10, "Midtown", (40.785091, -73.968285)),
            Graffiti(5, "Midtown", (40.786431, -73.969184)),
            Graffiti(1, "Midtown", (41.0, -74.0))]
        result = self.parks[0].graffitis_within_km(graffiti_instances, 1)
        self.assertEqual(result, 2)

    def test_graffitis_within_km_no_match(self):
        graffiti_instances = [Graffiti(1, "Faraway", (50.0, -80.0))]
        result = self.parks[0].graffitis_within_km(graffiti_instances, 1)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
