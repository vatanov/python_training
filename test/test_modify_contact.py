# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact_firstname_middlename(app):
    app.contact.modify_first_contact(Contact(firstname="Edited_qqqqq", middlename="Edited_eeeee"))
