from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
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


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*3
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    digits = string.digits + "+" + "-" + " "
    return "".join([random.choice(digits) for i in range(random.randrange(maxlen))])


testdata = [
        Contact(firstname=random_string("firstname", 8), middlename=random_string("middlename", 8),
        lastname=random_string("lastname", 8), nickname=random_string("nickname", 6), title=random_string("title", 10),
        homephone=random_phone(11), mobilephone=random_phone(11), workphone=random_phone(11))
    for i in range(n)
] + [Contact(firstname="", middlename="", lastname='', nickname="", title="", homephone="", mobilephone="", workphone="")]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))