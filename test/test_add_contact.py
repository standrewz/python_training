# -*- coding: utf-8 -*-
from contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.open_address_book_entry_page()
    app.contact.create_new_address_book_entry(Contact(last_name="Kolosov", first_name="Petr", middle_name="Sergeevich", nickname="petrucho", company="Ololo",
                                           address="St.Petersburg, Moskovskii pr., 100", birthday_day="3", email="Kolosov@mail.ru", mobile="89764563429",
                                           birthday_month="June", birthday_year="2000"))
    app.return_to_home_page()
    app.session.logout()





