from model.contact import Contact
from model.group import Group
import random


def test_remove_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testname", lastname="1234"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test_group", header="456"))
    random_group = random.choice(orm.get_group_list())
    random_contact = random.choice(orm.get_contact_list())
    if orm.check_add_contact_in_group(random_contact, random_group) is False:
        app.contact.add_contact_in_group(random_contact.id, random_group.id, random_group.name)
    app.contact.remove_contact_from_group(random_contact.id, random_group.id, random_group.name)
    assert orm.check_add_contact_in_group(random_contact, random_group) is False
