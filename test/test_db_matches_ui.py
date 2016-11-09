from model.group import Group
from model.contact import Contact


def test_group_list(app, db):
    ui_group_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    db_group_list = map(clean, db.get_group_list())
    assert sorted(ui_group_list, key = Group.id_or_max) == sorted(db_group_list, key = Group.id_or_max)


def test_contact_list(app, db):
    ui_contact_list = app.contact.get_contact_list()

    def clean(contact):
        return Contact(id=contact.id, lastname=contact.lastname.strip(), firstname=contact.firstname.strip(),
                     address=contact.address.strip(), email=contact.email.strip(), email2=contact.email.strip(),
                     email3=contact.email3.strip(), home=contact.home.strip(), mobile=contact.mobile.strip(),
                     work=contact.work.strip(), phone2=contact.phone2.strip())
    db_contact_list = map(clean, db.get_contact_list())
    assert sorted(ui_contact_list, key = Contact.id_or_max) == sorted(db_contact_list, key = Contact.id_or_max)
