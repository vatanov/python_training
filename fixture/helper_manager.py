from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class HelperManager:

    def __init__(self, app):
        self.app = app

    def start_helpers(self):
        self.app.session = SessionHelper(self)
        self.app.group = GroupHelper(self)
        self.app.contact = ContactHelper(self)