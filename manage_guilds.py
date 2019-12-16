# coding=utf-8

import discord
from discord.ext import commands as c

from private_info import kotori_guild_id, dip_test_guild_id
from cog_check import MainGuildOnly
from server_setting import _Bot, NotFoundGuildInListException


class ManageGuilds(c.Cog, name="M_Guild"):
    def __init__(self, bot: _Bot):
        self._bot = bot

        self._bot.get_bot().add_cog(CreateGuild(bot))
        self._bot.get_bot().add_cog(ListOfGuilds())
        self._bot.get_bot().add_cog(DeleteGuild(bot))


class CreateGuild(MainGuildOnly):
    def __init__(self, _bot: _Bot):
        self._bot = _bot

    @c.command(name="c_gld")
    async def create_guild(self, ctx: c.Context, arg: str):  # 10個を超えてサーバーを作ろうとするとエラーが出る問題は解消できてないよ
        created_guild = await ctx.bot.create_guild(arg)
        print(created_guild, created_guild.id)

        self._bot.add_setting(created_guild)

        invite_url = await self.create_invite_url(created_guild, "welcome")
        await ctx.send(invite_url)
        return

    @staticmethod
    async def create_invite_url(guild: discord.Guild, default_channel_name):
        created_ch = await guild.create_text_channel(default_channel_name)
        created_invite = await created_ch.create_invite()
        return created_invite.url


class ListOfGuilds(MainGuildOnly):
    @c.command(name="list_gld")
    async def list_guild(self, ctx: c.Context):
        paginator = c.Paginator()
        for gld in ctx.bot.guilds:
            paginator.add_line('{0}:{1}'.format(gld.id, gld.name))
        for page in paginator.pages:
            await ctx.send(page)
        return


class DeleteGuild(MainGuildOnly):
    def __init__(self, bot: _Bot):
        self._bot = bot

    @c.command(name="d_gld")
    async def delete_guild(self, ctx: c.Context, guild_id: int):  # 型変換できない場合と、潰す権限がない場合の例外処理がまだ
        if guild_id == kotori_guild_id or guild_id == dip_test_guild_id:
            printed_text = "そのサーバーは削除できません"
            await ctx.send(printed_text)
            return
        guild: discord.Guild = ctx.bot.get_guild(guild_id)
        if guild is not None:
            await ctx.send(guild.name + "を削除します。")
            """
            try:
                self._bot.delete_setting(guild)
            except NotFoundGuildInListException:
                await ctx.send("botに登録されているリストにこのサーバーは見つかりませんでした。")
            """
            await guild.delete()
            await ctx.send("削除しました")

            return
        await ctx.send("指定されたIDを持つサーバーは存在しません")
        return
