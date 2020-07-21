from sys import maxsize

class Contact:

    def __init__(self, lastname=None, firstname=None, id=None, middlename=None, nickname=None, company=None, address=None,
                 birthday_day=None, email=None, email2=None, email3=None, homephone=None, mobile=None, workphone=None, secondaryphone=None,
                 birthday_month=None, birthday_year=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.nickname = nickname
        self.company = company
        self.address = address
        self.birthday_day = birthday_day
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.middlename, self.nickname, self.company, self.address, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize