from model.contact import Contact


def test_delete_first_contact(app):
    old_contacts = app.contact.get_contacts_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test firstname", lastname="test lastname", address="test Address"))
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)



