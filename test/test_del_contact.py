from model.contact import Contact
import random


def test_delete_some_contact(app, orm, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test9", middlename="1234"))
    old_contacts = orm.get_contact_list()
    random_contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(random_contact.id)
    new_contacts = orm.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)