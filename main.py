# coding=utf-8

import discord
from private_info import token


class MyClient(discord.Client):
    async def on_ready(self):
        print('ログインしました\n')

    async def on_message(self, message):
        pass


client = MyClient()
client.run(token)
