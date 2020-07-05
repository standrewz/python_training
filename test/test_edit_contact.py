# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_group(app):
    if app.contact.count() == 0:
        app.contact.open_address_creation_page()
        app.contact.create_new_address_book_entry(Contact(last_name="Kolosov", first_name="Petr", middle_name="Sergeevich", nickname="petrucho", company="Ololo",
                                           address="St.Petersburg, Moskovskii pr., 100", birthday_day="3", email="Kolosov@mail.ru", mobile="89764563429",
                                           birthday_month="June", birthday_year="2000"))
        app.return_to_home_page()
    app.contact.edit_first_contact(Contact(last_name="New Kolosov", first_name="New Petr", middle_name="New Sergeevich", nickname="New petrucho", company="New Ololo",
                                           address="New St.Petersburg, Moskovskii pr., 100", birthday_day="13", email="New_Kolosov@mail.ru", mobile="99989764563429",
                                           birthday_month="April", birthday_year="2010"))