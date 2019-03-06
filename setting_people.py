# coding=utf-8

import discord
from discord.ext import commands as c
from cog_check import SubGuildOnly
from country import Country, country_list
from server_setting import _Bot


class SettingPeople(c.Cog):
    def __init__(self, bot: _Bot):
        self._bot = bot
        self._bot.get_bot().add_cog(AddRole())


class AddRole(SubGuildOnly):
    @c.command()
    async def add_player(self, ctx: c.Context):  # Playerという名称の役職がない場合に例外が発生する
        await ctx.author.add_roles(discord.utils.get(ctx.guild.roles, name="Player"))
        return

    @c.command()
    async def add_audience(self, ctx: c.Context):
        await ctx.author.add_roles(discord.utils.get(ctx.guild.roles, name="Audience"))

    @c.command()
    async def add_country(self, ctx: c.Context, _country):
        pass

