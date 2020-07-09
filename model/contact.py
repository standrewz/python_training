from sys import maxsize

class Contact:

    def __init__(self, last_name, first_name, middle_name=None, nickname=None, company=None, address=None, birthday_day=None, email=None, mobile=None, birthday_month=None, birthday_year=None, id=None):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.nickname = nickname
        self.company = company
        self.address = address
        self.birthday_day = birthday_day
        self.email = email
        self.mobile = mobile
        self.birthday_month = birthday_month
        self.birthday_year = birthday_year
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize