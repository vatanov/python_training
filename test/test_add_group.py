# -*- coding: utf-8 -*-
import pytest

from fixture.appliation import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.create(Group(name ="fghfghghjhkkiukl", header ="dfvbfgbgfnbhnhjnjh", footer ="dsfgbfdhtynuynjhmjkm"))
    app.session.logout()


def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
