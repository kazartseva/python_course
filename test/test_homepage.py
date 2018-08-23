import re
from random import randrange


def test_data_on_homepage(app):
    contacts = app.contact.get_contacts_list()
    index = randrange(len(contacts))
    contact_from_homepage = contacts[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_phones_from_homepage == merge_phone_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_emails_from_homepage == merge_email_like_on_homepage(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phone_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                    [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2]))))


def merge_email_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                             map(lambda x: clear(x),
                                 filter(lambda x: x is not None,
                                    [contact.email, contact.email2, contact.email3]))))
