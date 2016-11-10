# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.db import DbFixture
import random
import re


def get_random_group_id():
    db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(db.get_group_list()) > 0:
        random_group = random.choice(db.get_group_ids())
        id = int(re.sub("[(),]", "", random_group.id))
    else:
        id = "[none]"
    return id


def test_contacts_in_some_group(app, db):
    group_id = get_random_group_id()
    contacts_ui = app.contact.get_contacts_in_group(group_id)
    contacts_db = db.get_contacts_in_group(group_id)
    print()
    print(contacts_ui)
    print(contacts_db)
    assert contacts_db == contacts_ui
