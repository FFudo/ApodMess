from datetime import datetime

import requests

from config import API_KEY


class NasaDataManager:
    def __init__(self):
        self.today = datetime.now().strftime("%Y-%m-%d")

    def get_apod(self):
        url = "https://api.nasa.gov/planetary/apod"
        parameters = {
            "date": self.today,
            "api_key": API_KEY,
        }
        respones = requests.get(url=url, params=parameters)
        return respones.json()
