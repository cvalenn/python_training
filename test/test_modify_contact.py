from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="1234"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New firstname", lastname="New lastname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_contact_middlename(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="test", middlename="1234"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(middlename="New 345"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)