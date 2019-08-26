from model.group import Group

def test_change_group(app):
    app.group.change_group(Group("q", "w", "e"))