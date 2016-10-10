from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new(Contact(firstname="Contact for deletion", middlename="some middlename", lastname="some last name"))
    app.contact.del_first_contact()
