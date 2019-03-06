# coding=utf-8

import discord
from discord.ext import commands as c
from country import country_list, Country


class ArrangeGuild(c.Cog):
    def __init__(self, bot):
        self._bot = bot
        self._bot.add_cog(CreateRoles())
        self._bot.add_cog(ListRoles())
        self._bot.add_cog(Categories())
        self._bot.add_cog(Channels())


class CreateRoles(c.Cog):
    @c.command(name="s_roles")
    async def set_roles(self, ctx: c.Context):
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


class Categories(c.Cog):
    default_category_names = ["全体", "外交", "国内", "その他"]

    @c.command(name="l_ctgs")
    async def list_categories(self, ctx: c.Context):
        paginator = c.Paginator()
        for _ctg in ctx.guild.categories:
            paginator.add_line('{0}:{1}'.format(_ctg.id, _ctg.name))
        for page in paginator.pages:
            await ctx.send(page)
        return

    @c.command(name="s_ctgs")
    async def set_categories(self, ctx: c.Context):
        for category in ctx.guild.categories:
            await ctx.send("カテゴリ {0} を削除しました。".format(category.name))
            await category.delete()
        await ctx.send("既存のカテゴリを全て削除しました。")

        for category in Categories.default_category_names:
            created_category = await ctx.guild.create_category(category)
            await ctx.send("カテゴリ {0} を作成しました。".format(created_category.name))


class Channels(c.Cog):
    @c.command(name="l_chs")
    async def list_channels(self, ctx: c.Context):
        paginator = c.Paginator()
        for _ch in ctx.guild.channels:
            paginator.add_line('{0}:{1}'.format(_ch.id, _ch.name))
        for page in paginator.pages:
            await ctx.send(page)
        return
