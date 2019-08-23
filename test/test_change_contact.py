from model.contact import Contact

def test_change_contact(app):
    app.session.login("admin", "secret")
    app.contact.change(Contact("1", "2", "3", "4", "5"))
    app.session.logout()