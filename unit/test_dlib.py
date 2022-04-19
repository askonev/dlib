# -*- coding: utf-8 -*-

from lib.client import Client


def response():
    assert Client.user_choice({'1', '2'}) == {'1', '2'}
