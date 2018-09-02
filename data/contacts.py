from model.contact import Contact
import random
import string


constant = [
    Contact(firstname="firstname_1",
            middlename="middlename_1",
            lastname="lastname_1",
            nickname="nickname_1",
            title="title_1",
            company="company_1",
            address="address_1",
            homephone="homephone_1",
            mobilephone="mobilephone_1",
            workphone="workphone_1",
            fax="fax_1",
            email="email_1",
            email2="email2_1",
            email3="email3_1",
            homepage="homepage_1",
            address2="address2_1",
            phone2="phone2_1",
            notes="notes_1"),
    Contact(firstname="firstname_2",
            middlename="middlename_2",
            lastname="lastname_2",
            nickname="nickname_2",
            title="title_2",
            company="company_2",
            address="address_2",
            homephone="homephone_2",
            mobilephone="mobilephone_2",
            workphone="workphone_2",
            fax="fax_2",
            email="email_2",
            email2="email2_2",
            email3="email3_2",
            homepage="homepage_2",
            address2="address2_2",
            phone2="phone2_2",
            notes="notes_2")
]


def random_string(prefix, maxlenth):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlenth))])


testdata = [Contact(firstname="", middlename="", lastname="",
                      nickname="", title="", company="", address="", homephone="",
                      mobilephone="", workphone="", fax="", email="", email2="",
                      email3="",
                      homepage="", address2="", phone2="", notes="")] + \
           [Contact(firstname=random_string("firstname", 8),
                    middlename=random_string("middlename", 15),
                    lastname=random_string("lastname", 15),
                    nickname=random_string("nickname", 15),
                    title=random_string("title", 10),
                    company=random_string("company", 20),
                    address=random_string("address", 30),
                    homephone=random_string("homephone", 15),
                    mobilephone=random_string("mobilephone", 15),
                    workphone=random_string("workphone", 15),
                    fax=random_string("fax", 15),
                    email=random_string("email", 15),
                    email2=random_string("email2", 15),
                    email3=random_string("email3", 15),
                    homepage=random_string("homepage", 15),
                    address2=random_string("address2", 30),
                    phone2=random_string("phone2", 15),
                    notes=random_string("notes", 50)) for i in range(1)]
