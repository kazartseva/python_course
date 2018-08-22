# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Name", middlename="Middle name", lastname="Last name",
                               nickname="Nickname", title="Title", company="Company", address="Address", home="6666666",
                               mobile="555555", work="444444", fax="1111", email="email1", email2="email2",
                               email3="email3",
                               homepage="www.homapage.com", bday="1", bmonth="March", byear="1856", aday="2",
                               amonth="May",
                               ayear="1890", address2="address", phone2="home", notes="notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

