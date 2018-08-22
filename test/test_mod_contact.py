from model.contact import Contact


def test_modify_first_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname="Modified")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test firstname", lastname="test lastname", address="test Address"))
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



