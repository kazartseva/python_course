# -*- coding: utf-8 -*-
from model.contact import Contact


def test_create_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Name 5", middlename="Middle name 5", lastname="Last name 5",
                      nickname="Nickname", title="Title", company="Company", address="Address", homephone="6666666",
                      mobilephone="555555", workphone="444444", fax="1111", email="email1", email2="email2",
                      email3="email3",
                      homepage="www.homapage.com", bday="1", bmonth="March", byear="1856", aday="2",
                      amonth="May",
                      ayear="1890", address2="address", phone2="home", notes="notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

