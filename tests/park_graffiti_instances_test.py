"""
Shichao Tian
It's a unittest for create instances functions
"""
from models.graffiti import Graffiti
from models.park import Park
from utils.create_instances import (
    create_park_instances, create_graffiti_instances)
import unittest


class TestParkGraffitiCreation(unittest.TestCase):
    def test_create_park_instances(self):
        data = [
            {'name': 'Central Park', 'neighbour': 'Downtown', 'coordinates': (
                40.785091, -73.968285)},
            {'name': 'Prospect Park', 'neighbour': 'Brooklyn', 'coordinates': (
                40.660204, -73.968956)}
        ]
        result = create_park_instances(data)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Park)
        self.assertEqual(result[0].name, 'Central Park')

    def test_create_graffiti_instances(self):
        data = [
            {'count': 5, 'neighbour': 'Downtown', 'coordinates': (
                40.712776, -74.005974)},
            {'count': 3, 'neighbour': 'Bronx', 'coordinates': (
                40.844782, -73.864827)}
        ]
        result = create_graffiti_instances(data)
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Graffiti)
        self.assertEqual(result[0].count, 5)


if __name__ == '__main__':
    unittest.main()
