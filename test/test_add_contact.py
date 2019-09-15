# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*3
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    digits = string.digits + "+" + "-" + " "
    return "".join([random.choice(digits) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname='', nickname="", title="")] + [
        Contact(firstname=random_string("firstname", 8), middlename=random_string("middlename", 8),
        lastname=random_string("lastname", 8), nickname=random_string("nickname", 6), title=random_string("title", 10),
        homephone=random_phone(11), mobilephone=random_phone(11), workphone=random_phone(11))
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




