import re
from random import randrange
from model.contact import Contact


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert sorted(contact_from_home_page.all_phones_from_home_page) == sorted(merge_phones_like_on_home_page(contact_from_edit_page))


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone


def test_name_contact(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    assert contact_from_home_page.lastname == app.contact.get_contact_info_from_edit_page(index).lastname
    assert contact_from_home_page.firstname == app.contact.get_contact_info_from_edit_page(index).firstname


def test_email_and_address_contact(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)
    assert clear(contact_from_home_page.address) == merge_address_like_on_home_page(contact_from_edit_page)


def test_all_contacts_on_the_page(app, db):
    ui_contacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for c in range(len(ui_contacts)):
        assert ui_contacts[c].firstname == db_contacts[c].firstname
        assert ui_contacts[c].lastname == db_contacts[c].lastname
        assert ui_contacts[c].address == db_contacts[c].address
        assert ui_contacts[c].all_email_from_home_page == merge_email_like_on_home_page(db_contacts[c])
        assert ui_contacts[c].all_phones_from_home_page == merge_phones_like_on_home_page(db_contacts[c])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.address]))))


