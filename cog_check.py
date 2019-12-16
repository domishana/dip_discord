# coding=utf-8

import discord
from discord.ext import commands as c
from private_info import dip_test_guild_id, owner_id


class MainGuildOnly(c.Cog):
    async def cog_check(self, ctx: c.Context):
        return ctx.guild.id == dip_test_guild_id

    async def cog_command_error(self, ctx, error):
        if type(error) == c.errors.CheckFailure:
            await ctx.send("このコマンドは {0} サーバーでのみ実行できます。".format(ctx.bot.get_guild(dip_test_guild_id).name))
        return


class SubGuildOnly(c.Cog):
    async def cog_check(self, ctx: c.Context):
        return ctx.guild.id != dip_test_guild_id

    async def cog_command_error(self, ctx, error):
        if type(error) == c.errors.CheckFailure:
            await ctx.send("このコマンドは {0} サーバー以外でのみ実行できます。".format(ctx.bot.get_guild(dip_test_guild_id).name))
        return


async def is_gm(ctx):
    return discord.utils.get(ctx.guild.roles, name="GM") in ctx.author.roles

async def is_kari_gm(ctx):
    return discord.utils.get(ctx.guild.roles, name="+GM") in ctx.author.roles

async def is_owner(ctx):
    return ctx.author.id == owner_id

async def is_gm_or_owner(ctx):
    return is_gm(ctx) or is_kari_gm(ctx) or is_owner(ctx)
