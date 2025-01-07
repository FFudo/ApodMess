from discord_messenger import DiscordWebhook
from nasa_api import NasaDataManager


def run_app():
    nasa_data = NasaDataManager()
    data = nasa_data.get_apod()

    discord = DiscordWebhook()
    if data["media_type"] == "image":
        discord.send_apod(data=data)
    elif data["media_type"] == "video":
        discord.send_avod(data=data)


if __name__ == "__main__":
    run_app()
