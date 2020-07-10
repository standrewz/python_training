from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    app.return_to_home_page()
    if app.contact.count() == 0:
        app.contact.create_new_address_book_entry(Contact(last_name="Kolosov", first_name="Petr", middle_name="Sergeevich", nickname="petrucho", company="Ololo",
                                           address="St.Petersburg, Moskovskii pr., 100", birthday_day="3", email="Kolosov@mail.ru", mobile="89764563429",
                                           birthday_month="June", birthday_year="2000"))
        app.return_to_home_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts



