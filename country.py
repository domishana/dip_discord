# coding=utf-8
import discord


class Country:
    def __init__(self, _name, _colour_code, _short=None, _alphabet=None):
        self._name = _name
        self._short = _short
        self._alphabet = _alphabet
        self._colour_code = _colour_code

    def get_name(self):
        return self._name

    def get_short(self):
        return self._short

    def get_colour(self):
        return discord.Colour(self._colour_code)

    def get_alphabet(self):
        return self._alphabet


austria = Country("オーストリア", 0xad1457, _short="墺", _alphabet="A")
england = Country("イギリス", 0x9B59B6, _short="英", _alphabet="E")
france = Country("フランス", 0x3498db, _short="仏", _alphabet="F")
germany = Country("ドイツ", 0xe67e22, _short="独", _alphabet="G")
italy = Country("イタリア", 0x2ecc71, _short="伊", _alphabet="I")
russia = Country("ロシア", 0xE7E9F3, _short="露", _alphabet="R")
turkey = Country("トルコ", 0xf1c40f, _short="土", _alphabet="T")

country_list = [austria, england, france, germany, italy, russia, turkey]
