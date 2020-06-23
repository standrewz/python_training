# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_address_book_entry_page()
    app.contact.create_new_address_book_entry(Contact(last_name="Kolosov", first_name="Petr", middle_name="Sergeevich", nickname="petrucho", company="Ololo",
                                           address="St.Petersburg, Moskovskii pr., 100", birthday_day="3", email="Kolosov@mail.ru", mobile="89764563429",
                                           birthday_month="June", birthday_year="2000"))
    app.return_to_home_page()
    app.session.logout()





