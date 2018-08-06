from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test firstname", lastname="test lastname", address="test Address"))
    app.contact.delete_first_contact()



