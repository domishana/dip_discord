# coding=utf-8

import discord
from discord.ext import commands as c

from private_info import token, kotori_guild_id, dip_test_guild_id
from cog_test import CogTest
from manage_guilds import ManageGuilds
from arrange_guild import ArrangeGuild
from setting_people import SettingPeople

from server_setting import ServerSettings, _Bot

bot = _Bot(c.Bot(command_prefix="!!", case_insensitive=True), ServerSettings())
_bot = bot.get_bot()


@_bot.listen()
async def on_ready():
    print('ログインしました\n')

_bot.add_cog(CogTest(bot))
_bot.add_cog(ManageGuilds(bot))
_bot.add_cog(ArrangeGuild(bot))
_bot.add_cog(SettingPeople(bot))

_bot.run(token)
