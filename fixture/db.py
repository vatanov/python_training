import mysql.connector
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database = name, user=user, password=password)
        self.connection.autocommit = True

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_group_ids(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id from group_list")
            for row in cursor:
                (id) = row
                list.append(Group(id=str(id)))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("""select id, firstname, lastname, address, home, mobile, work, email, email2, email3,
                           phone2 from addressbook where deprecated='0000-00-00 00:00:00'""")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address = address, home = home,
                                    mobile = mobile, work = work, email = email, email2 = email2, email3 = email3,
                                    phone2 = phone2))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("""SELECT addressbook.id, addressbook.firstname, addressbook.lastname, addressbook.address,
                           addressbook.home, addressbook.mobile, addressbook.work, addressbook.email, addressbook.email2,
                           addressbook.email3, addressbook.phone2 FROM addressbook
                           JOIN address_in_groups WHERE addressbook.id = address_in_groups.id
                           AND addressbook.deprecated = '0000-00-00 00:00:00' AND address_in_groups.group_id=%s""" % group_id)
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address = address, home = home,
                                    mobile = mobile, work = work, email = email, email2 = email2, email3 = email3,
                                    phone2 = phone2))
        finally:
            cursor.close()
        return list






    def destroy(self):
        self.connection.close()
