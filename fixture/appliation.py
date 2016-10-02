from selenium.webdriver.firefox.webdriver import WebDriver
# from fixture.session import SessionHelper
# from fixture.group import GroupHelper
# from fixture.contact import ContactHelper
from fixture.helper_manager import HelperManager


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        # self.session = SessionHelper(self)
        # self.group = GroupHelper(self)
        # self.contact = ContactHelper(self)
        self.session = HelperManager(self)
        self.group = HelperManager(self)
        self.contact = HelperManager(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def go_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()
