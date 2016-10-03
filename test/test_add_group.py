# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.create(Group(name ="fghfghghjhkkiukl", header ="dfvbfgbgfnbhnhjnjh", footer ="dsfgbfdhtynuynjhmjkm"))
    app.session.logout()


def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
