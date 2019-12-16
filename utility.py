# coding=utf-8

import discord
from discord.ext import commands as c

from server_setting import _Bot
from cog_check import SubGuildOnly, is_gm_or_owner
from arrange_guild import CreateRoles, Categories, CreateChannels

class Utility(c.Cog):
    def __init__(self, bot: _Bot):
        self._bot = bot

        self._bot.get_bot().add_cog(InitialSetting(bot))



class InitialSetting(SubGuildOnly):
    def __init__(self, bot: _Bot):
        self._bot = bot

    @c.command(name="init_set")
    @c.check(is_gm_or_owner)
    async def initial_setting(self, ctx: c.Context):
        roles = None
        for cog_ in self._bot.get_bot().cogs.values():
            if type(cog_) is CreateRoles:
                roles = cog_
                break
        await roles.set_roles(ctx)

        categories = None
        for cog_ in self._bot.get_bot().cogs.values():
            if type(cog_) is Categories:
                categories = cog_
                break
        await categories.set_categories(ctx)

        channels = None
        for cog_ in self._bot.get_bot().cogs.values():
            if type(cog_) is CreateChannels:
                channels = cog_
                break
        await channels.create_channels(ctx)

        for ch in ["general", "welcome", "General"]:
            ch = discord.utils.get(ctx.guild.channels, name=ch)
            await ch.edit(category=discord.utils.get(ctx.guild.categories, name="その他"))

