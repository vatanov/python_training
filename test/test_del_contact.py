from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Contact for deletion", middlename="some middlename", lastname="some last name"))
    old_contacts = app.contact.get_contact_list()
    app.contact.del_first_contact()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
