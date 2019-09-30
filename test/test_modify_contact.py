from model.contact import Contact
import random


def test_modify_contact(app, orm, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", lastname="1234"))
    old_contacts = orm.get_contact_list()
    random_contact = random.choice(old_contacts)
    contact = Contact(firstname="New firstname", lastname="New lastname")
    app.contact.modify_contact_by_id(random_contact.id, contact)
    new_contacts = orm.get_contact_list()
    old_contacts[old_contacts.index(random_contact)] = contact
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_modify_contact_middlename(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="test", middlename="1234"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(middlename="New 345"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)