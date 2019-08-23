

def test_delete_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.delete()
    app.session.logout()