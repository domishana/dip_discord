# coding=utf-8

import discord
from discord.ext import commands as c


class SettingPeople(c.Cog):
    def __init__(self, bot):
        self._bot = bot
        self._bot.add_cog(AddRole())


class AddRole(c.Cog):
    @c.command()
    async def add_player(self, ctx: c.Context):  # Playerという名称の役職がない場合に例外が発生する
        await ctx.author.add_roles(discord.utils.get(ctx.guild.roles, name="Player"))
        return
