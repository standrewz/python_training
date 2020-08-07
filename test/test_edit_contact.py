# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_edit_some_contact(app, db, check_ui):
    app.return_to_home_page()
    if app.contact.count() == 0:
        app.contact.open_address_creation_page()
        app.contact.create_new_address_book_entry(Contact(lastname="Kolosov", firstname="Petr", middlename="Sergeevich", nickname="petrucho", company="Ololo",
                                                          address="St.Petersburg, Moskovskii pr., 100", birthday_day="3", email="Kolosov@mail.ru", homephone="6357864", mobile="89764563429",
                                                          workphone="38786537", secondaryphone="634221", birthday_month="June", birthday_year="2000"))
        app.return_to_home_page()
    old_contacts = db.get_contact_list()
    random_index = randrange(len(old_contacts))
    contact = old_contacts[random_index]
    updated_contact = Contact(lastname="New Kolosov", firstname="New Petr", middlename="New Sergeevich", nickname="New petrucho", company="New Ololo",
                      address="New St.Petersburg, Moskovskii pr., 100", birthday_day="13", email="New_Kolosov@mail.ru", homephone="3124664", mobile="99989764563429", workphone="4515161",
                      secondaryphone="4354643643", birthday_month="April", birthday_year="2010")
    updated_contact.id = contact.id
    app.contact.edit_contact_by_id(contact.id, updated_contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[random_index] = updated_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)