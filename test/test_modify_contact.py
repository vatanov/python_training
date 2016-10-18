# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact_firstname_and_middlename(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Contact for modification", middlename="some middlename", lastname="some last name"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Edited_qqqqq", lastname="Edited_eeeee")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)