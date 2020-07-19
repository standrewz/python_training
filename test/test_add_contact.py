from model.contact import Contact

def test_add_contact(app):
    app.return_to_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="Kolosov", firstname="Petr", middlename="Sergeevich", nickname="petrucho", company="Ololo",
                      address="St.Petersburg, Moskovskii pr., 100", birthday_day="3", email="Kolosov@mail.ru", homephone="2434556", mobile="89764563429",
                      workphone="6454665", secondaryphone="5365436", birthday_month="June", birthday_year="2000")
    app.contact.create_new_address_book_entry(contact)
    app.return_to_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





