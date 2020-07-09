from model.contact import Contact

def test_add_contact(app):
    app.return_to_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(last_name="Kolosov", first_name="Petr", middle_name="Sergeevich", nickname="petrucho", company="Ololo",
                                           address="St.Petersburg, Moskovskii pr., 100", birthday_day="3", email="Kolosov@mail.ru", mobile="89764563429",
                                           birthday_month="June", birthday_year="2000")
    app.contact.create_new_address_book_entry(contact)
    app.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





