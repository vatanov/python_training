from model.contact import Contact
import random


def test_add_contact_in_group(app, db):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Contact for deletion", middlename="some middlename", lastname="some last name"))
    contacts = db.get_contact_list()
    group_id = app.group.get_random_group_id()
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(contact.id, group_id)
    contact_ui = app.contact.get_contacts_in_group(group_id)
    contact_db = db.get_contacts_in_group(group_id)
    assert contact_db == contact_ui
