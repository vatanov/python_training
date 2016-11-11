# -*- coding: utf-8 -*-


def test_contacts_in_some_group(app, db):
    group_id = app.group.get_random_group_id()
    contacts_ui = app.contact.get_contacts_in_group(group_id)
    contacts_db = db.get_contacts_in_group(group_id)
    assert contacts_db == contacts_ui
