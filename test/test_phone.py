def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contacts_view_page(0)
    contact_from_edit_page = app.contact.get_contact_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2
