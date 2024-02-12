import os
import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/v2"
TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY', 'Custom Message / Key does not exist')

class FlightSearch:
    # this class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        # return "TESTING" code for now, to ensure it's working. We can get Tequila API data later:
        dest_code = "TESTING Data within the IATA Code Column"
        return dest_code