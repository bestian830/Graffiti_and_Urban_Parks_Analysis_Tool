"""
Shichao Tian
Final Project --- Class Graffiti
This is the Model file store classes and functions
"""


class Graffiti:
    """
    Represents a graffiti incident with its associated details.

    Attributes:
        count (int): The count of graffiti occurrences recorded.
        neighbour (str): The neighbourhood where the graffiti is located.
        coordinates (tuple): A tuple containing latitude and longitude where
        the graffiti was found.

    Methods:
        graffiti_in_neighbour(graffiti): Calculates the total graffiti in each
        neighbourhood.
        most_graff_neighbour(graff_count): Identifies the neighbourhood with
        the maximum number of graffiti.
        less_graff_neighbour(graff_count): Identifies the neighbourhood with
        the minimum number of graffiti.
    """
    def __init__(self, count, neighbour, coordinates):
        """
        Purpose:
            Initialize a Graffiti instance with count, neighbourhood, and
            coordinates.

        Parameters:
            count (int): Number of graffiti occurrences.
            neighbour (str): Name of the neighbourhood the graffiti is in.
            coordinates (tuple): Latitude and longitude of the graffiti
            location.
        """
        self.count = count
        self.neighbour = neighbour
        self.coordinates = coordinates

    def graffiti_in_neighbour(graffiti):
        """
        Purpose:
            Calculate the total graffitis in each neighbours

        Parameters:
            graffiti: list of graffiti instances

        Returns:
            dict: include the count of graffiti in neighbours

        Raises:
            Nothing
        """
        graff_count = {}

        for g in graffiti:
            neighbour = g.neighbour
            count = int(g.count)
            if neighbour not in graff_count:
                graff_count[neighbour] = count
            else:
                graff_count[neighbour] += count

        return graff_count

    def __str__(self):
        return (
            f"Graffiti Count: {self.count}, "
            f"Neighbourhood: {self.neighbour}"
            f"Coordinates: {self.coordinates}")
