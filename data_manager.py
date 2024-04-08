import requests
import os

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT")
headers = {
    "Authorization": os.environ.get("AUTHORIZATION")
}


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        self.destination_data = requests.get(SHEETY_PRICES_ENDPOINT, headers=headers).json()["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )

            print(response.text)

