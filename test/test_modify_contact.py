# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_modify_some_contact_firstname_and_middlename(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Contact for modification", middlename="some middlename",
                                       lastname="some last name"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Edited_qqqqq", lastname="Edited_eeeee")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact, contact.id)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
