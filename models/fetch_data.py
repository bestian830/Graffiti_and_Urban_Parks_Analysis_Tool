"""
Shichao Tian
Final project fetch_csv_data files
"""
import requests


def fetch_csv_data(url):
    """
    Purpose:
        Fetch data from given url

    Parameters:
        url: csv data url

    Returns:
        list: A list containing each row of CSV data, each row is a string.

    Raises:
        Exception: If response is not successful.
    """
    response = requests.get(url)
    if response.status_code != 200:
        error_message = ('Failed to fetch the data with status code: {}'
                         .format(response.status_code))
        raise requests.HTTPError(error_message)
    else:
        return response.text.splitlines()


def parse_csv_data(raw_data):
    """
    Purpose:
        Parse CSV data.

    Parameters:
        raw_data: A list of rows of the original CSV data, each row is a
        string.

    Returns:
        Returns a list where each element is a list of strings representing a
        row of the CSV

    Raises:
        ValueError: If the data is incorrectly formatted.

    >>> parse_csv_data(['Name;NeighbourhoodName', 'Park1;Neighborhood1'])
    [{'Name': 'Park1', 'NeighbourhoodName': 'Neighborhood1'}]
    >>> parse_csv_data(['Name;NeighbourhoodName', 'Park1'])
    Traceback (most recent call last):
        ...
    ValueError: Row does not match headers in length. Check the CSV format.
    """
    # Clean and seperate title string
    headers = raw_data[0].lstrip('\ufeff').split(';')
    # Initialize a empty list to save the data after parsed
    parsed_data = []

    for data in raw_data[1:]:
        # Seperate each line
        values = data.split(';')
        if len(values) != len(headers):
            raise ValueError("Row does not match headers in length. Check the"
                             " CSV format.")
        # Create a empty dict to store the data after parse
        data_dict = {}
        for i in range(len(headers)):
            key = headers[i]
            value = values[i]
            data_dict[key] = value

        # Put the dict into the empty list
        parsed_data.append(data_dict)

    return parsed_data


def clean_data(parsed_data):
    """
    Purpose:
        Clean and reformat the parsed CSV data into structured dictionaries
        based on specific keys.

    Parameters:
        parsed_data (list): A list of dictionaries, where each dictionary
        represents a row of CSV data.

    Returns:
        list: A list of dictionaries with cleaned data structured into specific
        formats depending on the content.

    Raises:
        KeyError: If an expected key is missing in any of the data
        dictionaries.
        ValueError: If data conversion (like converting to float) fails due to
        incorrect data format.
    """
    cleaned_data = []

    for data in parsed_data:
        if 'Name' in data:
            if 'GoogleMapDest' not in data:
                raise KeyError("Missing 'GoogleMapDest' key in park data.")
            coordinates_str = data.get('GoogleMapDest', '0,0')
            coordinates_split = coordinates_str.split(',')
            lat_is_valid = (
                coordinates_split[0].strip().replace('.', '', 1).isdigit())
            lon_is_valid = (
                coordinates_split[1].strip().replace('.', '', 1).isdigit())

            if not (lat_is_valid or not lon_is_valid):
                raise ValueError(
                    f"Invalid coordinates format: {coordinates_str}")
            lat = float(coordinates_split[0].strip())
            lon = float(coordinates_split[1].strip())
            park_info = {
                'name': data.get('Name'),
                'neighbour': data.get('NeighbourhoodName'),
                'coordinates': (lat, lon),
                'hectare': data.get('Hectare')}
            cleaned_data.append(park_info)
        else:
            if 'geo_point_2d' not in data:
                raise KeyError("Missing 'geo_point_2d' key in graffiti data.")
            coordinates_str = data.get('geo_point_2d', '0,0')
            coordinates_split = coordinates_str.split(',')
            lat_is_valid = (
                coordinates_split[0].strip().replace('.', '', 1).isdigit())
            lon_is_valid = (
                coordinates_split[1].strip().replace('.', '', 1).isdigit())

            if not (lat_is_valid or not lon_is_valid):
                raise ValueError(
                    f"Invalid coordinates format: {coordinates_str}")

            lat = float(coordinates_split[0].strip())
            lon = float(coordinates_split[1].strip())
            graf_info = {
                'count': data.get('COUNT'),
                'neighbour': data.get('Geo Local Area'),
                'coordinates': (lat, lon)}
            cleaned_data.append(graf_info)

    return cleaned_data
