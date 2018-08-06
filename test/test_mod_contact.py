from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test firstname", lastname="test lastname", address="test Address"))
    app.contact.modify_first_contact(Contact(firstname="Modified"))



