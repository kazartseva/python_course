# -*- coding: utf-8 -*-
from contact import Contact
from group import Group
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Name", middlename="Middle name", lastname="Last name",
                               nickname="Nickname", title="Title", company="Company", address="Address", home="6666666",
                               mobile="555555", work="444444", fax="1111", email="email1", email2="email2",
                               email3="email3",
                               homepage="www.homapage.com", bday="1", bmonth="March", byear="1856", aday="2",
                               amonth="May",
                               ayear="1890", address2="address", phone2="home", notes="notes"))
    app.logout()
