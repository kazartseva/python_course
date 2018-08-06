# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    app.contact.create(Contact(firstname="Name", middlename="Middle name", lastname="Last name",
                               nickname="Nickname", title="Title", company="Company", address="Address", home="6666666",
                               mobile="555555", work="444444", fax="1111", email="email1", email2="email2",
                               email3="email3",
                               homepage="www.homapage.com", bday="1", bmonth="March", byear="1856", aday="2",
                               amonth="May",
                               ayear="1890", address2="address", phone2="home", notes="notes"))

