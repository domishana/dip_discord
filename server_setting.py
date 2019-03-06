# coding=utf-8

import discord


class NotFoundGuildInListException(Exception):
    pass


class ServerSetting():
    def __init__(self, _guild: discord.Guild):
        self._guild = _guild
        self._country_list = None

    def __str__(self):
        return self._guild.name + "の設定"

    def get_guild(self):
        return self._guild


class ServerSettings():
    def __init__(self):
        self._server_list = []

    def add_guild(self, ss: ServerSetting):
        self._server_list.append(ss)
        return

    def get_settings(self):
        return self._server_list

    def delete_guild(self, _guild: discord.Guild):
        guild_list = [setting.get_guild() for setting in self._server_list]
        try:
            _index = guild_list.index(_guild)
        except ValueError:
            raise NotFoundGuildInListException
        self._server_list.pop(_index)
        return


class _Bot():
    def __init__(self, _bot, _setting: ServerSettings):
        self._bot = _bot
        self._settings = _setting

    def get_bot(self):
        return self._bot

    def get_setting(self):
        return self._settings.get_settings()

    def add_setting(self, _guild: discord.Guild):
        self._settings.add_guild(ServerSetting(_guild))

    def delete_setting(self, _guild: discord.Guild):
        self._settings.delete_guild(_guild)
