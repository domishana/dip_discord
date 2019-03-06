# coding=utf-8

from discord.ext import commands as c
from server_setting import _Bot


class CogTest(c.Cog):
    def __init__(self, bot: _Bot):
        self._bot = bot

    @c.command()
    async def test1(self, ctx: c.Context):
        await ctx.send("!!test2")
        return

    @c.command()
    async def test2(self, ctx: c.Context):
        await ctx.send("test2が呼ばれました")
        return

    @c.command()
    async def test3(self, ctx: c.Context):
        for _gld in self._bot.get_setting():
            print(_gld)
        return
