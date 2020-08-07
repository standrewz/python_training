from model.contact import Contact

def test_add_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    app.return_to_home_page()
    old_contacts = db.get_contact_list()
    app.contact.create_new_address_book_entry(contact)
    app.return_to_home_page()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
