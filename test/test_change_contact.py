from model.contact import Contact

def test_change_contact(app):
    app.contact.change(Contact("1", "2", "3", "4", "5"))