from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="1234"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New 123"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="1234"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename="New 345"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)