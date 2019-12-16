# coding=utf-8

import discord
from discord.ext import commands as c
from cog_check import SubGuildOnly, is_gm_or_owner
from country import Country, country_list
from server_setting import _Bot


class SettingPeople(c.Cog):
    def __init__(self, bot: _Bot):
        self._bot = bot
        self._bot.get_bot().add_cog(AddRole())
        self._bot.get_bot().add_cog(DeleteRole())
        self._bot.get_bot().add_cog(ManageRole())


class AddRole(SubGuildOnly):
    @c.command()
    @c.check(is_gm_or_owner)
    async def add_player(self, ctx: c.Context, member_id: int):  # Playerという名称の役職がない場合に例外が発生する
        await self.add_role_to_member(ctx, discord.utils.get(ctx.guild.roles, name="Player"),
                                      discord.utils.get(ctx.guild.members, id=member_id))
        return

    @c.command()
    @c.check(is_gm_or_owner)
    async def add_audience(self, ctx: c.Context, member_id: int):
        await self.add_role_to_member(ctx, discord.utils.get(ctx.guild.roles, name="Audience"),
                                      discord.utils.get(ctx.guild.members, id=member_id))
        return

    @c.command()
    @c.check(is_gm_or_owner)
    async def add_role(self, ctx: c.Context, member_id: int, role_name):
        await self.add_role_to_member(ctx, discord.utils.get(ctx.guild.roles, name=role_name),
                                      discord.utils.get(ctx.guild.members, id=member_id))

    async def add_role_to_member(self, ctx, role, member):
        await member.add_roles(role)
        await ctx.send("{0}に役職{1}を付与しました。".format(member.name, role.name))
        return


class DeleteRole(SubGuildOnly):
    @c.command()
    @c.check(is_gm_or_owner)
    async def remove_role(self, ctx: c.Context, member_id: int, role_name):
        await self.remove_role_from_member(ctx, discord.utils.get(ctx.guild.roles, name=role_name),
                                      discord.utils.get(ctx.guild.members, id=member_id))

    async def remove_role_from_member(self, ctx, role, member):
        await member.remove_roles(role)
        await ctx.send("{0}から役職{1}を消去しました。".format(member.name, role.name))
        return


class ManageRole(SubGuildOnly):
    @c.command()
    @c.check(is_gm_or_owner)
    async def move_role_position(self, ctx: c.Context, role_id: discord.Role, new_posit: int):
        await role_id.edit(position=new_posit)