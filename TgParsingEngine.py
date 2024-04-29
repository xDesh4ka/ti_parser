import asyncio
import datetime

from typing import AsyncGenerator

from pyrogram import Client
from pyrogram.types import Message

from HttpSender import HttpSender
from OutputMessage import OutputMessage
from properties import API_ID, API_HASH


class TgChannelParsingEngine:
    def __init__(self, back_url, channel_ids: list):
        print("Parsing Engine Initialized")
        self.channel_ids: list = channel_ids
        self.http_sender = HttpSender(back_url)

    def run(self):
        for channel_id in self.channel_ids:
            asyncio.run(self.process_messages(channel_id))
            # asyncio.run( self.process_messages_write_to_file(channel_id))

    # Получение сообщений и отправка на бэк
    async def process_messages(self, channel_id: int):
        messages = await self.get_output_messages_from_channel(channel_id)
        for message in messages:
            if message.text is None:
                continue
            self.send_to_collector(message.to_json())

    def send_to_collector(self, message):
        self.http_sender.send(message)

    async def get_output_messages_from_channel(self, channel_id: int):
        return await self.parse(channel_id)

    async def parse(self, channel_id: int):
        async with Client(name='my_session', api_id=API_ID, api_hash=API_HASH) as client:
            #chat_history: AsyncGenerator[Message, None] = client.get_chat_history(channel_id, offset_date= datetime.datetime.today().replace(hour=0, minute=0, second=0))
            chat_history: AsyncGenerator[Message, None] = client.get_chat_history(channel_id)
            result = [OutputMessage(message.date, message.text) async for message in chat_history]
            return result

    # Получение сообщений и запись в файл
    async def process_messages_write_to_file(self, channel_id: int):
        file = open(f"${channel_id.__str__()}.json", "w")
        file.write("[")
        messages = await self.get_output_messages_from_channel(channel_id)
        message_index = 0
        messages_len = len(messages)
        for message in messages:
            message_index += 1
            # Пропускаем пустые сообщения
            if message.text is None:
                continue

            file.write(message.to_json().replace("\\n", ""))
            if message_index != messages_len:
                file.write(",\n")

        file.write("]")
        file.close()
