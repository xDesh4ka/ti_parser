import json

import requests


class HttpSender:
    def __init__(self, url: str):
        self.url = url

    def send(self, body: str):
        try:
            print(body)
            responce = requests.post(url=self.url, data=body, headers={'Content-type': 'application/json'}).json()
            print(responce)
        except Exception as e:
            print(f"Ошибка отправки запроса: {self.url}\n{e}")
