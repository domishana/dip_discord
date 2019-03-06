# coding=utf-8

import discord
from discord.ext import commands as c
from country import country_list, Country


class ArrangeGuild(c.Cog):
    def __init__(self, bot):
        self._bot = bot
        self._bot.add_cog(CreateRoles())
        self._bot.add_cog(ListRoles())


class CreateRoles(c.Cog):
    @c.command(name="c_roles")
    async def create_roles(self, ctx: c.Context):
        if discord.utils.get(ctx.guild.roles, name="Player") is not None:
            print("既に役職を生成済みのため、実行できません。")
            await ctx.send("既に役職を生成済みのため、実行できません。")
            return

        _role = await ctx.guild.create_role(name="Player")
        print(_role.name)
        for _country in country_list:
            _role = await ctx.guild.create_role(name=_country.get_name(), colour=_country.get_colour())
            print(_role.name)
        _role = await ctx.guild.create_role(name="Audience")
        print(_role.name)
        return


class ListRoles(c.Cog):
    @c.command(name="l_roles")
    async def list_roles(self, ctx: c.Context):
        paginator = c.Paginator()
        for _role in ctx.guild.roles:
            paginator.add_line('{0}:{1}'.format(_role.id, _role.name))
        for page in paginator.pages:
            await ctx.send(page)
        return
