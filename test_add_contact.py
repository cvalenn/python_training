# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact(firstname="wer", middlename="ert", lastname='342', nickname="rty", title="rty", company="rty", address="rty", home="rty", mobile="rty", work="rty", fax="rty", email="rty",
                            email2="rty", email3="rty", homepage="rty", address2="rty", phone2="rty", notes="rty"))
    app.logout()


def test_empty_contact(app):
    app.login("admin", "secret")
    app.create_contact(Contact(firstname="", middlename="", lastname='', nickname="", title="", company="", address="", home="", mobile="", work="", fax="", email="",
                            email2="", email3="", homepage="", address2="", phone2="", notes=""))
    app.logout()
