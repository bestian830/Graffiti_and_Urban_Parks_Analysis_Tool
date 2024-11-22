"""
Shichao Tian
Final Project --- Class park
This is the Model file store classes and functions
"""
from utils.functions import haversine


class Park:
    """
    Represents a park with its associated details.

    Attributes:
        name (str): The name of the park.
        neighbour (str): The neighbourhood where the park is located.
        coordinates (tuple): A tuple containing latitude and longitude of the
        park.

    Methods:
        park_in_neighbour(parks): Calculates the total number of parks in each
        neighbourhood.
        most_park_neighbour(park_count): Identifies the neighbourhood with the
        maximum number of parks.
        less_park_neighbour(park_count): Identifies the neighbourhood with the
        minimum number of parks.
        graffitis_within_km(graffiti_instances, km): Counts how many graffiti
        instances are within a certain distance of the park.
    """
    def __init__(self, name, neighbour, coordinates):
        """
        Purpose:
            Initialize a Park instance with name, neighbourhood, and
            coordinates.

        Parameters:
            name (str): Name of the park.
            neighbour (str): Name of the neighbourhood the park is in.
            coordinates (tuple): Latitude and longitude of the park.
        """
        self.name = name
        self.neighbour = neighbour
        self.coordinates = coordinates

    def park_in_neighbour(park):
        """
        Purpose:
            Calculate the total parks in each neighbours

        Parameters:
            park: list of graffiti instances

        Returns:
            dict: include the count of graffiti in neighbours

        Raises:
            Nothing
        """
        park_count = {}

        for p in park:
            neighbour = p.neighbour
            if neighbour not in park_count:
                park_count[neighbour] = 1
            else:
                park_count[neighbour] += 1

        return park_count

    def graffitis_within_km(self, graffiti_instances, km):
        """
        Purpose:
            Calculate the number of graffitis within 5 km of the park

        Parameters:
            graffiti_instances(list): A list of Graffiti instances

        Returns:
            int: The count of graffitis within 5 km

        Raises:
            Nothing
        """
        count = 0
        for graffiti in graffiti_instances:
            distance = haversine(self.coordinates[0],
                                 self.coordinates[1],
                                 graffiti.coordinates[0],
                                 graffiti.coordinates[1])
            if distance <= km:
                count += 1
        return count

    def __str__(self):
        return (
            f"Park: {self.name}, "
            f"Neighbour: {self.neighbour}, "
            f"Coordinates: {self.coordinates}")
