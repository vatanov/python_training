# -*- coding: utf-8 -*-
import pytest
from group import Group
from appliation import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username = "admin", password = "secret")
    app.create_group(Group(name = "fghfghghjhkkiukl", header = "dfvbfgbgfnbhnhjnjh", footer = "dsfgbfdhtynuynjhmjkm"))
    app.logout()


def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
