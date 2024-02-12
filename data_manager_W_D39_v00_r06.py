import requests
import json, pprint

SHEETY_PRICES_URL_ENDPOINT = "https://api.sheety.co/cdae1a11efe5f92ecbe6d22972bba27d/sirisFlightDeals/prices"

#This class is responsible for talking to the Google Sheet.
class DataManager:
    # def __init__(self, JSON_data_in_PyDict_format):
    def __init__(self):
        self.destination_data = {}

    def get_request_for_getting_destination_data(self):
        # using the Sheety API to GET the data from that Google Sheet, and then print it out:
        sheety_API_GET_response = requests.get(url=SHEETY_PRICES_URL_ENDPOINT)  #  removed .json from end. no need for it!! it's not part of the endpoint. It goes on the next line:
        data = sheety_API_GET_response.json()
        self.destination_data = data["prices"]  # prices is the name of the sheet and also the List of Dictionaries
        # print(f"The sheety_API_GET_response: {sheety_API_GET_response.raise_for_status()}")

        # print("The pretty/formatted destination_data: ")
        # pprint.pprint(self.destination_data)
        return self.destination_data


    def update_destination_codes(self):   # remove: def destination_data(self): already used
        for city in self.destination_data:   #remove () after destination_data
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_URL_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)



    # get_request_for_getting_destination_data(self)

# we've got to created an instance of the class, before we can call the method on the instance:
# data_manager_instance = DataManager()

# data_manager_instance.get_request_for_getting_destination_data()






















        # if JSON_data_in_PyDict_format is None:
#             JSON_data_in_PyDict_format = {
#                 "prices": [
#                     {
#                         "city": "Tokyo",
#                         "iataCode": "HND",
#                         "lowestPrice": 500,
#                         "id": 2
#                     },
#                     {
#                         "city": "Sydney",
#                         "iataCode": "SYD",
#                         "lowestPrice": 550,
#                         "id": 3
#                     },
#                     {
#                         "city": "Frankfurt",
#                         "iataCode": "FRA",
#                         "lowestPrice": 500,
#                         "id": 4
#                     },
#                     {
#                         "city": "Cairo",
#                         "iataCode": "CAI",
#                         "lowestPrice": 500,
#                         "id": 5
#                     },
#                     {
#                         "city": "Honolulu",
#                         "iataCode": "HNL",
#                         "lowestPrice": 500,
#                         "id": 6
#                     },
#                     {
#                         "city": "San Francisco",
#                         "iataCode": "SFO",
#                         "lowestPrice": 200,
#                         "id": 7
#                     },
#                     {
#                         "city": "Singapore",
#                         "iataCode": "SIN",
#                         "lowestPrice": 500,
#                         "id": 8
#                     }
#                 ]
#             }
#         self.JSON_data_in_PyDict_format = JSON_data_in_PyDict_format
#
# data_manager = DataManager(JSON_data_in_PyDict_format)
#
#     # print(JSON_data)
#     # pprint((JSON_data))
#         self.sheet_data = JSON_data['prices']
#         self.prices_of_json_data = JSON_data
#
#     # Python Dictionary dict:
#     # prices = {sheet_data['prices']}   # extra: [0]['city']['iataCode']['lowestPrice']}
#     # pprint(prices)
