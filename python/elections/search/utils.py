from functools import lru_cache

import requests

from elections.settings import API_URL


HEADERS = {"Accept": "application/json"}


@lru_cache(maxsize=100)
def get_upcoming_elections(state_ocd_id, place_ocd_id):
    """
    Fetches upcoming elections for a given state and place.

    Parameters:
        state_ocd_id (str): The OCD ID of the state (e.g., "ocd-division/country:us/state:ny").
        place_ocd_id (str): The OCD ID of the place (e.g., "ocd-division/country:us/state:ny/place:albany").

    Returns:
        dict: A dictionary containing the upcoming elections data for the given state and place.

    Raises:
        requests.exceptions.HTTPError: If there is an HTTP error during the API request.
        requests.exceptions.RequestException: If there is a non-HTTP-related error during the API request.

    Note:
        This function utilizes the 'lru_cache' decorator to cache the results of previous requests
        to reduce API calls and improve performance. The cache can store up to 100 recent results.

    Example:
        >>> state_id = "ocd-division/country:us/state:ny"
        >>> place_id = "ocd-division/country:us/state:ny/place:albany"
        >>> upcoming_elections = get_upcoming_elections(state_id, place_id)
        >>> print(upcoming_elections)
        {
            'description': 'New York Municipal Election',
            'date': '2023-08-15T00:00:00Z',
            'district-divisions': [...],
            ...
        }
    """
    params = {"district-divisions": f"{state_ocd_id},{place_ocd_id}"}
    response = requests.get(API_URL, params=params, headers=HEADERS)

    response.raise_for_status()

    return response.json()


def generate_ocd_ids(**kwargs):
    """
    Generates Open Civic Data (OCD) IDs for a given state and city.

    Parameters:
        **kwargs: Keyword arguments representing the state and city.
            state (str): The state abbreviation (e.g., "NY" for New York).
            city (str): The name of the city.

    Returns:
        tuple: A tuple containing two strings:
            - The OCD ID of the state (e.g., "ocd-division/country:us/state:ny").
            - The OCD ID of the place (e.g., "ocd-division/country:us/state:ny/place:albany").

    Example:
        >>> state_id, place_id = generate_ocd_ids(state="NY", city="Albany")
        >>> print(state_id)
        'ocd-division/country:us/state:ny'
        >>> print(place_id)
        'ocd-division/country:us/state:ny/place:albany'
    """
    state = kwargs.get("state").lower()
    city = kwargs.get("city").lower().replace(" ", "_")
    state_ocd_id = f"ocd-division/country:us/state:{state}"
    place_ocd_id = f"{state_ocd_id}/place:{city}"

    return state_ocd_id, place_ocd_id
