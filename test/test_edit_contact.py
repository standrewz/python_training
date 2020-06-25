# -*- coding: utf-8 -*-
from model.contact import Contact

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(last_name="New Kolosov", first_name="New Petr", middle_name="New Sergeevich", nickname="New petrucho", company="New Ololo",
                                           address="New St.Petersburg, Moskovskii pr., 100", birthday_day="13", email="New_Kolosov@mail.ru", mobile="99989764563429",
                                           birthday_month="April", birthday_year="2010"))
    app.session.logout()