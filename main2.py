# coding=utf-8

import discord
from discord.ext import commands as c

from private_info import token, kotori_guild_id, dip_test_guild_id
from cog_test import CogTest
from manage_guilds import ManageGuilds
from arrange_guild import ArrangeGuild
from setting_people import SettingPeople

bot = c.Bot(command_prefix="!!", case_insensitive=True)


@bot.listen()
async def on_ready():
    print('ログインしました\n')

bot.add_cog(CogTest())
bot.add_cog(ManageGuilds(bot))
bot.add_cog(ArrangeGuild(bot))
bot.add_cog(SettingPeople(bot))

bot.run(token)
