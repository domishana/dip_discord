# coding=utf-8

from discord.ext import commands as c


class CogTest(c.Cog):
    @c.command()
    async def test1(self, ctx: c.Context):
        await ctx.send("!!test2")
        return

    @c.command()
    async def test2(self, ctx: c.Context):
        await ctx.send("test2が呼ばれました")
        return
