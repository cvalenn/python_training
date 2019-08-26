# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="wer", middlename="ert", lastname='342', nickname="rty", title="rty"))


def test_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname='', nickname="", title=""))
