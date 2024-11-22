"""
Shichao Tian
Final project functions files
"""
import math
from models.fetch_data import fetch_csv_data, parse_csv_data, clean_data
import re


def data_get():
    """
    Purpose:
        Get the data prepare

    Parameter:
        Nothing

    Returns:
        list of dict: park data
        list of dict: graff data

    Raises:
        Nothing
    """
    park_url = ("https://opendata.vancouver.ca/api/explore/v2.1/catalog/"
                "datasets/parks/exports/csv?lang=en&timezone=America%2F"
                "Los_Angeles&use_labels=true&delimiter=%3B")
    graffiti_url = ("https://opendata.vancouver.ca/api/explore/v2.1/catalog/"
                    "datasets/graffiti/exports/csv?lang=en&timezone=America"
                    "%2FLos_Angeles&use_labels=true&delimiter=%3B")
    park_raw_data = fetch_csv_data(park_url)
    graff_raw_data = fetch_csv_data(graffiti_url)
    park_parsed_data = parse_csv_data(park_raw_data)
    graff_parsed_data = parse_csv_data(graff_raw_data)
    park_cleaned_data = clean_data(park_parsed_data)
    graff_cleaned_data = clean_data(graff_parsed_data)
    return park_cleaned_data, graff_cleaned_data


def menu():
    """
    Purpose:
        Print the menu information

    Parameters:
        Nothing

    Returns:
        Nothing

    Raises:
        Nothing
    """
    print("\nBonjour! Let's explore the relations between parks and "
          "graffitis!\n\nShall we look at the park or the graffiti first?")
    return


def haversine(lat1, lon1, lat2, lon2):
    """
    Purpose:
        Calculate the great circle distance between two points

    Parameters:
        lat1: float latitude of point1
        lon1: float longitute of point1
        lat2: float latitude of point2
        lon2: float longitute of point2

    Returns:
        distance

    Raises:
        ValueError: If any latitude or longitude values are outside their
        valid ranges (-90 to 90 for latitudes and -180 to 180 for longitudes).
        TypeError: If any of the inputs are not float or convertible to float.

    >>> haversine(48.8566, 2.3522, 34.0522, -118.2437) # Paris to Los Angeles
    9085.508815906822
    >>> haversine(52.5200, 13.4050, 55.7558, 37.6173) # Berlin to Moscow
    1608.8313354358454
    >>> haversine(-90, 0, 90, 0)  # Poles
    20015.086796020572
    >>> haversine(0, 0, 0, 0)  # Same point
    0.0
    """
    for coordinate in [lat1, lon1, lat2, lon2]:
        if not isinstance(coordinate, (int, float)):
            raise TypeError(
                f"Coordinate values must be int or float, got"
                f"{type(coordinate).__name__} instead.")

    if not (-90 <= lat1 <= 90) or not (-90 <= lat2 <= 90):
        raise ValueError("Latitude values must be between -90 and 90 degrees.")
    if not (-180 <= lon1 <= 180) or not (-180 <= lon2 <= 180):
        raise ValueError(
            "Longitude values must be between -180 and 180 degrees.")

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = (
        math.sin(dlat/2)**2 +
        math.cos(lat1) *
        math.cos(lat2) *
        math.sin(dlon/2)**2)
    c = 2 * math.asin(math.sqrt(a))
    radius_earth = 6371
    distance = c * radius_earth
    return distance


def option():
    """
    Purpose:
        Prompt the user to choose an option between parks, graffiti, or
        quitting the application.

    Parameters:
        None

    Returns:
        str: The user's choice as a lowercase string ('p', 'g', 'q').

    Raises:
        Nothing
    """
    choice = input("p for park\ng for graffiti\nq for quit\n").lower()
    return choice


def graff_option():
    """
    Purpose:
        Prompt the user to decide if they want to explore the amount of
        graffiti near the park.

    Parameters:
        None

    Returns:
        str: The user's decision as a lowercase string ('y' for yes, 'n' for
        no).

    Raises:
        Nothing
    """
    choice = input("\nNow we know the number of parks.\nLet's explore the"
                   " amount of graffiti near the park."
                   "\ny for yes\nn for no\n").lower()
    return choice


def park_option():
    """
    Purpose:
        Prompt the user to decide if they want to explore the amount of parks
        near the graffiti locations.

    Parameters:
        None

    Returns:
        str: The user's decision as a lowercase string ('y' for yes, 'n' for
        no).

    Raises:
        Nothing
    """
    choice = input("\nNow we know the number of graffitis.\nLet's explore the "
                   "amount of graffiti near the park.\ny for yes"
                   "\nn for no\n").lower()
    return choice


def ask_km():
    """
    Purpose:
        Prompt the user to specify the radius in kilometers for exploring
        nearby features.

    Parameters:
        None

    Returns:
        float: The radius in kilometers specified by the user.

    Raises:
        ValueError: If the input is not a valid float.
    """
    input_str = input("\nHow many kilometers do we want to explore?\n")
    # Check if the input string can be converted to a float
    if not re.match(r'^\d+(\.\d+)?$', input_str):
        raise ValueError(
            "Invalid input: Please enter a valid positive numerical value for"
            " kilometers.")

    km = float(input_str)
    return km


def get_review():
    """
    Purpose:
        Ask the user for their feedback and a score for the final project.

    Parameters:
        None

    Returns:
        str: The user's review of the project.

    Raises:
        Nothing
    """
    review = input("\nThank you for test. Do you like my final project?\n"
                   "What score you would give me?\n")
    return review


def back():
    """
    Purpose:
        Inform the user to check the histogram and prepare to return to the
        main menu.

    Parameters:
        None

    Returns:
        None

    Raises:
        Nothing
    """
    print("\nPlease check the histogram.\nThen let's back to main menu.")


def back_menu():
    """
    Purpose:
        Notify the user that returning to the main menu is a good choice.

    Parameters:
        None

    Returns:
        None

    Raises:
        Nothing
    """
    print("\nGood choice! Let's back to main menu.")
    return


def invalid():
    """
    Purpose:
        Inform the user that they made an invalid choice and that they will be
        directed back to the main menu.

    Parameters:
        None

    Returns:
        None

    Raises:
        Nothing
    """
    print("\nBad choice! We'll back to main menu.")
    return


def appreciate():
    """
    Purpose:
        Express appreciation to the user and wish them a good day.

    Parameters:
        None

    Returns:
        None

    Raises:
        Nohting
    """
    print("\nGood to know! Have a nice day! : )")
    return
