from sys import maxsize


class Contact:

    def __init__(self, id=None,
                 firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 title=None,
                 company=None,
                 address=None,
                 homephone=None,
                 mobilephone=None,
                 workphone=None,
                 all_phones_from_homepage=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 all_emails_from_homepage=None,
                 bday=None,
                 bmonth=None,
                 byear=None,
                 aday=None,
                 amonth=None,
                 ayear=None,
                 address2=None,
                 phone2=None,
                 notes=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_homepage = all_emails_from_homepage
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes

    def __repr__(self):
        return "Contact (id = %s, lastname = %s, firstname = %s)" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) \
               and self.lastname == other.lastname \
               and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
