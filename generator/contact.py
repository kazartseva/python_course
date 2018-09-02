from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
                    notes=random_string("notes", 50)) for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
