from model.contact import Contact
from model.group import Group
import random
import time

def test_remove_some_contact_from_group(app, orm, check_ui):
    app.return_to_home_page()
    if len(orm.get_contact_list()) == 0:
        app.contact.create_new_address_book_entry(Contact(lastname="Kolosov", firstname="Petr", middlename="Sergeevich", nickname="petrucho", company="Ololo",
                                                          address="St.Petersburg, Moskovskii pr., 100", birthday_day="3", email="Kolosov@mail.ru", mobile="89764563429",
                                                          birthday_month="June", birthday_year="2000"))
        app.return_to_home_page()
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
        app.return_to_home_page()

    # Get some group with linked contacts
    groups = orm.get_groups_with_linked_contacts()
    if len(groups) == 0:
        # Get random group for adding contact
        groups = orm.get_group_list()
        group = random.choice(groups)
        # Get random contact which is not added to group yet
        unlinked_contacts = orm.get_contacts_not_in_group(group)
        contact = random.choice(unlinked_contacts)
        # Add selected contact to group
        app.contact.add_contact_to_group(contact, group)
    else:
        group = random.choice(groups)
        # Get some contact linked to group
        linked_contacts = orm.get_contacts_in_group(group)
        contact = random.choice(linked_contacts)
    # Remove contact from group
    app.contact.remove_contact_from_group(contact, group)
    # Check that disassociation was successful
    linked_contacts = orm.get_contacts_in_group(group)
    assert contact not in linked_contacts



