from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testname", lastname="1234"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test_group", header="456"))
    if len(orm.check_free_contacts()) == 0:
        app.contact.create(Contact(firstname="testname", lastname="1234"))
    random_contact = random.choice(orm.check_free_contacts())
    random_group = random.choice(orm.get_group_list())
    app.contact.add_contact_in_group(random_contact.id, random_group.id, random_group.name)
    assert orm.check_add_contact_in_group(random_contact, random_group) is True



