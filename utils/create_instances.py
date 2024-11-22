"""
Shichao Tian
Final project instances create files
"""
from models.graffiti import Graffiti
from models.park import Park


def create_park_instances(park_data):
    """
    Purpose:
        Create a list of Park instances from provided data.

    Parameters:
        park_data (list): List of dictionaries, each containing the data
        needed to initialize a Park instance.

    Returns:
        list: List of initialized Park instances.

    Raises:
        Nothing
    """
    park_instances = []
    for item in park_data:
        park = Park(
            name=item.get('name'),
            neighbour=item.get('neighbour'),
            coordinates=item.get('coordinates'))
        park_instances.append(park)
    return park_instances


def create_graffiti_instances(graffiti_data):
    """
    Purpose:
        Create a list of Graffiti instances from provided data.

    Parameters:
        graffiti_data (list): List of dictionaries, each containing the data
        needed to initialize a Graffiti instance.

    Returns:
        list: List of initialized Graffiti instances.

    Raises:
        Nothing
    """
    graffiti_instances = []
    for item in graffiti_data:
        graffiti = Graffiti(
            count=item.get('count', 0),
            neighbour=item.get('neighbour'),
            coordinates=item.get('coordinates'))
        graffiti_instances.append(graffiti)
    return graffiti_instances
