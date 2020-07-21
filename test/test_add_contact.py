from model.contact import Contact
import pytest
import random
import string
import datetime
import re

def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*5
    s = "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
    # to avoid test fail because of symbol '
    return re.sub("'", "", s)

def random_text_string(maxlen):
    symbols = string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number_string(minlen, maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(minlen, maxlen))])

def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def random_email(length):
    domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
    letters = string.ascii_lowercase[:12] + string.digits
    def get_random_domain(domains):
        return random.choice(domains)
    def get_random_name(letters, length):
        return "".join(random.choice(letters) for i in range(length))
    def generate_random_email(length):
        return get_random_name(letters, length) + "@" + get_random_domain(domains)
    return generate_random_email(length)

test_birthdays = [
    random_date(datetime.date(1930, 1, 1), datetime.date(2015, 1, 1))
    for i in range(5)
    ]

testdata = [
    Contact(lastname=random_text_string(20), firstname=random_text_string(20), middlename=random_text_string(20),
            nickname=random_string(10), company=random_text_string(20), address=random_string(50),
            birthday_day=str(test_birthdays[i].day), email=random_email(10), homephone=random_number_string(0,10),
            mobile=random_number_string(5,12), workphone=random_number_string(0,4), secondaryphone=random_number_string(0,2),
            birthday_month=test_birthdays[i].strftime("%B"), birthday_year=str(test_birthdays[i].year)
            )
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    app.return_to_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_address_book_entry(contact)
    app.return_to_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





