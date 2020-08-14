import re
from random import randrange
from model.contact import Contact

def test_phones_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()[0]
    app.contact.open_contact_to_edit_by_index(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page()
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_phones_on_contact_view_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    app.contact.open_contact_to_view_by_index(0)
    contact_info_from_view_page = app.contact.get_contact_info_from_view_page()
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_info_from_view_page)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobile, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3])))

def test_contact_data_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    for db_contact in contacts_from_db:
        db_contact.all_phones_from_home_page = merge_phones_like_on_home_page(db_contact)
        db_contact.all_emails_from_home_page = merge_emails_like_on_home_page(db_contact)
    contacts_from_db = sorted(contacts_from_db, key=Contact.id_or_max)
    contacts_from_home_page = sorted(contacts_from_home_page, key=Contact.id_or_max)
    # Basic check
    assert contacts_from_home_page == contacts_from_db
    # Extended checks
    for index in range(len(contacts_from_db)):
        assert clear(contacts_from_db[index].address) == clear(contacts_from_home_page[index].address)
        assert contacts_from_db[index].all_phones_from_home_page == contacts_from_home_page[index].all_phones_from_home_page
        assert contacts_from_db[index].all_emails_from_home_page == contacts_from_home_page[index].all_emails_from_home_page

def test_contact_data_on_edit_page(app, db):
    contacts_from_db = db.get_contact_list()
    for contact in contacts_from_db:
        app.contact.open_contact_to_edit_by_id(contact.id)
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page()
        verify_contact_data(contact, contact_from_edit_page)

def test_contact_data_on_view_page(app, db):
    contacts_from_db = db.get_contact_list()
    for contact in contacts_from_db:
        app.contact.open_contact_to_view_by_id(contact.id)
        contact_from_view_page = app.contact.get_contact_info_from_view_page()
        verify_contact_phones(contact, contact_from_view_page)

def verify_contact_data(expected_contact, actual_contact):
    assert expected_contact.firstname == actual_contact.firstname
    assert expected_contact.lastname == actual_contact.lastname
    assert expected_contact.address == actual_contact.address
    assert expected_contact.email == actual_contact.email
    assert expected_contact.email2 == actual_contact.email2
    assert expected_contact.email3 == actual_contact.email3
    verify_contact_phones(expected_contact, actual_contact)

def verify_contact_phones(expected_contact, actual_contact):
    assert expected_contact.homephone == actual_contact.homephone
    assert expected_contact.mobile == actual_contact.mobile
    assert expected_contact.workphone == actual_contact.workphone
    assert expected_contact.secondaryphone == actual_contact.secondaryphone

def verify_contact_phones(expected_contact, actual_contact):
    assert expected_contact.homephone == actual_contact.homephone
    assert expected_contact.mobile == actual_contact.mobile
    assert expected_contact.workphone == actual_contact.workphone
    assert expected_contact.secondaryphone == actual_contact.secondaryphone







