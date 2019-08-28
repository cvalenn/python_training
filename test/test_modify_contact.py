from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="1234"))
    app.contact.modify_first_contact(Contact(firstname="New 123"))


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="1234"))
    app.contact.modify_first_contact(Contact(middlename="New 345"))