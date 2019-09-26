import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, title, home, mobile, work from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, title, home, mobile, work) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title, homephone=home,
                                    mobilephone=mobile, workphone=work))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()