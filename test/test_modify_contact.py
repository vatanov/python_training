# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact_firstname_and_middlename(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Contact for modification", middlename="some middlename", lastname="some last name"))
    app.contact.modify_first_contact(Contact(firstname="Edited_qqqqq", middlename="Edited_eeeee"))
