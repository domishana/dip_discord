# coding=utf-8

import discord
from private_info import token


class MyClient(discord.Client):
    async def on_ready(self):
        print('ログインしました\n')

    async def on_message(self, message: discord.Message):
        message.channel: discord.TextChannel
        if message.author == self.user:
            return

        if message.content.startswith('!!'):
            u = message.author.id
            _cmd = message.content[2::]
            c = _cmd.split(" ")
            cmd = c[0].lower()
            arg = c[1::] if len(c) >= 2 else []

            if cmd.startswith('c_gld'):
                if arg == []:
                    return
                guild_id = await self.create_guild(arg[0])
                print(guild_id)
                return

            if cmd.startswith('list_gld'):
                printed_text = '```'
                for gld in self.guilds:
                    printed_text += '{0}:{1}\n'.format(gld.id, gld.name)
                printed_text += '```'
                await message.channel.send(printed_text)
        pass


client = MyClient()
client.run(token)
