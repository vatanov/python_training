# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def go_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def create_new_contact(self, wd, contact):
        # Go to "Add new" link
        wd.find_element_by_link_text("add new").click()
        # Fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[13]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[13]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[10]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[6]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[6]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def test_add_contact1(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_new_contact(wd, Contact(firstname="qqqqq", middlename="eeeee", lastname="aaaaa", nickname="ffffff",
                           title="ccccc", company="hhhhhhhhh", address="ddddddddddddd, 55555555",
                           home="222222222222", mobile="333333333333", work="44444444444", fax="555555555555555555",
                           email="bbbb@hhhh.oo", email2="nnn@lll.yy", email3="pppp@oooo.eee", homepage="www.kkkk.hh",
                           byear="1970", ayear="2010", address2="jjjjjjjjjjjjjjjjjjjj, 8888888",
                           phone2="yyyyyyyyyyyyyyyy", notes="ff ggggggg ssss kkkkk bbbbbb"))
        self.go_to_home_page(wd)
        self.logout(wd)

    def test_add_contact2(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_new_contact(wd, Contact(firstname="qaz", middlename="wsx", lastname="edcrfv", nickname="qwertyu",
                           title="sdfdsffsdfdsf", company="hjkjhliuiytufgfdbv", address="dfgfhtyhjmjh, 567",
                           home="34564654654654", mobile="34545435345", work="3456467657", fax="76876876867665",
                           email="qwe@df.io", email2="wsx@ghj.yu", email3="sdsd@fgfhfghfg.edf", homepage="www.fghff.gh",
                           byear="1980", ayear="2000", address2="dfgdfgfdgfdgrdgrertyfdg, 34342534",
                           phone2="ertrytryrt", notes="rgfdgfdgtfgthtyhygjyhfth"))
        self.go_to_home_page(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
