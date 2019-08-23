from model.group import Group

def test_change_group(app):
    app.session.login("admin", "secret")
    app.group.change_group(Group("q", "w", "e"))
    app.session.logout()