# coding=utf-8

import discord
from discord.ext import commands as c
from country import country_list, Country
from itertools import combinations


class ArrangeGuild(c.Cog):
    def __init__(self, bot):
        self._bot = bot
        self._bot.add_cog(CreateRoles())
        self._bot.add_cog(ListRoles())
        self._bot.add_cog(Categories())
        self._bot.add_cog(Channels(bot))


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
    async def set_categories(self, ctx: c.Context):  # 2回目実行すると、カテゴリ内のチャンネルは削除されずカテゴリのみ削除される問題点がある
        for category in ctx.guild.categories:
            await ctx.send("カテゴリ {0} を削除しました。".format(category.name))
            await category.delete()
        await ctx.send("既存のカテゴリを全て削除しました。")

        for category in Categories.default_category_names:
            created_category = await ctx.guild.create_category(category)
            await ctx.send("カテゴリ {0} を作成しました。".format(created_category.name))


class Channels(c.Cog):
    def __init__(self, bot):
        self._bot = bot
        self._bot.add_cog(CreateChannels())

    @c.command(name="l_chs")
    async def list_channels(self, ctx: c.Context):
        paginator = c.Paginator()
        for _ch in ctx.guild.channels:
            paginator.add_line('{0}:{1}'.format(_ch.id, _ch.name))
        for page in paginator.pages:
            await ctx.send(page)
        return


class CreateChannels(c.Cog):
    @c.command(name="c_chs")
    async def create_channels(self, ctx: c.Context):
        await self.create_channels_for_all(ctx)
        await self.create_channels_for_diplomacy(ctx)
        await self.create_channels_for_domestic(ctx)

    async def create_channels_for_all(self, ctx: c.Context):
        if discord.utils.get(ctx.guild.channels, name="全員") is not None:
            await ctx.send("既に全体カテゴリ内のチャンネルを生成済みのため実行できませんでした。")
            return

        _category = discord.utils.get(ctx.guild.categories, name="全体")

        created_for_all = await ctx.guild.create_text_channel(name="全員", category=_category)
        await ctx.send("<#{0}> を作成しました。".format(created_for_all.id))

        created_for_all_players = await ctx.guild.create_text_channel(name="全体外交", category=_category)
        await ctx.send("<#{0}> を作成しました。".format(created_for_all_players.id))
        return

    async def create_channels_for_diplomacy(self, ctx: c.Context):
        if discord.utils.get(
                ctx.guild.channels, name=(country_list[0].get_short() + "-" + country_list[1].get_short())) is not None:
            await ctx.send("既に外交カテゴリ内のチャンネルを生成済みのため実行できませんでした。")
            return

        _category = discord.utils.get(ctx.guild.categories, name="外交")

        for double_country in combinations(country_list, 2):
            created = await ctx.guild.create_text_channel(
                name=(double_country[0].get_short() + '-' + double_country[1].get_short()), category=_category)
            await ctx.send("<#{0}> を作成しました。".format(created.id))
        return

    async def create_channels_for_domestic(self, ctx: c.Context):
        if discord.utils.get(ctx.guild.channels, name=(country_list[0].get_name() + "国内")) is not None:
            await ctx.send("既に国内カテゴリ内のチャンネルを生成済みのため実行できませんでした。")
            return

        _category = discord.utils.get(ctx.guild.categories, name="国内")

        for country in country_list:
            created = await ctx.guild.create_text_channel(name=(country.get_name() + "国内"), category=_category)
            await ctx.send("<#{0}> を作成しました。".format(created.id))
        return
