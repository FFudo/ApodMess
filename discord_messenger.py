import requests

from config import DISCORD_URL


class DiscordWebhook:
    def __init__(self):
        self.url = DISCORD_URL
        self.username = "Space Bot"
        self.avatar_url = "https://img.freepik.com/free-vector/rocket-background-flat-style_23-2147904992.jpg?t=st=1736193697~exp=1736197297~hmac=cc99828c66d856526fcd6524a3fdf7345ea9ff3ea29ac1fb138d4e66a6e7782d&w=1380"

    def send_apod(self, data):
        message = {
            "username": self.username,
            "avatar_url": self.avatar_url,
            "content": data["date"] + "\n" + data["explanation"],
            "embeds": [{"image": {"url": data["hdurl"]}}],
        }
        response = requests.post(self.url, json=message)
        response.raise_for_status()
        print(response.content)

    def send_avod(self, data):
        message = {
            "username": self.username,
            "avatar_url": self.avatar_url,
            "content": data["date"] + "\n" + data["explanation"] + "\n" + data["url"],
        }
        response = requests.post(self.url, json=message)
        response.raise_for_status()
        print(response.content)
