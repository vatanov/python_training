# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    return random.randrange(1, 34, 1)

def random_month():
    return random.randrange(1, 13, 1)

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                    homepage="", bday="1", bmonth="1", byear="", aday="1", amonth="1", ayear="",
                    address2="", phone2="", notes="")] + \
           [Contact(firstname=random_string("f_name", 5), middlename=random_string("m_name", 5),
                   lastname=random_string("l_name", 5), nickname=random_string("n_name", 5),
                   title=random_string("title", 5), company=random_string("company", 5),
                   address=random_string("addr", 15), home=random_string("home", 5), mobile=random_string("mobile", 5),
                   work=random_string("work", 5), fax=random_string("fax", 5), email=random_string("email", 5),
                   email2=random_string("email_2", 5), email3=random_string("email_3", 5),
                   homepage=random_string("h_page", 15), bday=random_day(), bmonth=random_month(),
                   byear=random_string("", 4), aday=random_day(), amonth=random_month(), ayear=random_string("", 4),
                   address2=random_string("addr", 20), phone2=random_string("phone_2", 5),
                   notes=random_string("notes", 30))
           for i in range(5)
           ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
