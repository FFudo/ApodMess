import json

from discord_messenger import DiscordWebhook
from nasa_api import NasaDataManager


def run_app():
    nasa_data = NasaDataManager()
    data = nasa_data.get_apod()

    if data["media_type"] == "image":
        discord = DiscordWebhook()
        discord.send_apod(data=data)


if __name__ == "__main__":
    run_app()
