from model.group import Group
import random


def test_modify_group_name(app, orm, check_ui):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = orm.get_group_list()
    random_group = random.choice(old_groups)
    group = Group(name="New group")
    app.group.modify_group_by_id(random_group.id, group)
    new_groups = orm.get_group_list()
    old_groups[old_groups.index(random_group)] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_header(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name="test"))
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)