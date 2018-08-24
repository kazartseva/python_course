# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlenth):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlenth))])


testdata = [Contact(firstname="", middlename="", lastname="",
                      nickname="", title="", company="", address="", homephone="",
                      mobilephone="", workphone="", fax="", email="", email2="",
                      email3="",
                      homepage="", address2="", phone2="", notes="")] + \
           [Contact(firstname=random_string("firstname", 8),
                    middlename=random_string("middlename", 15),
                    lastname=random_string("lastname", 15),
                    nickname=random_string("nickname", 15),
                    title=random_string("title", 10),
                    company=random_string("company", 20),
                    address=random_string("address", 30),
                    homephone=random_string("homephone", 15),
                    mobilephone=random_string("mobilephone", 15),
                    workphone=random_string("workphone", 15),
                    fax=random_string("fax", 15),
                    email=random_string("email", 15),
                    email2=random_string("email2", 15),
                    email3=random_string("email3", 15),
                    homepage=random_string("homepage", 15),
                    address2=random_string("address2", 30),
                    phone2=random_string("phone2", 15),
                    notes=random_string("notes", 50)) for i in range(1)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

