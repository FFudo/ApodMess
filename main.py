import json

from nasa_api import NasaDataManager


def run_app():
    nasa_data = NasaDataManager()
    data = nasa_data.get_apod()
    with open("output.json", "w") as f:
        json.dump(data, f, indent=6)


if __name__ == "__main__":
    run_app()
