from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    app.return_to_home_page()
    if app.contact.count() == 0:
        app.contact.create_new_address_book_entry(Contact(lastname="Kolosov", firstname="Petr", middlename="Sergeevich", nickname="petrucho", company="Ololo",
                                                          address="St.Petersburg, Moskovskii pr., 100", birthday_day="3", email="Kolosov@mail.ru", mobile="89764563429",
                                                          birthday_month="June", birthday_year="2000"))
        app.return_to_home_page()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



