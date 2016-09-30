# -*- coding: utf-8 -*-
import pytest

from fixture.appliation import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact1(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.create_new(Contact(firstname="qqqqq", middlename="eeeee", lastname="aaaaa", nickname="ffffff",
                                   title="ccccc", company="hhhhhhhhh", address="ddddddddddddd, 55555555",
                                   home="222222222222", mobile="333333333333", work="44444444444", fax="555555555555555555",
                                   email="bbbb@hhhh.oo", email2="nnn@lll.yy", email3="pppp@oooo.eee", homepage="www.kkkk.hh",
                                   byear="1970", ayear="2010", address2="jjjjjjjjjjjjjjjjjjjj, 8888888",
                                   phone2="yyyyyyyyyyyyyyyy", notes="ff ggggggg ssss kkkkk bbbbbb"))
    app.session.logout()


def test_add_contact2(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.create_new(Contact(firstname="qaz", middlename="wsx", lastname="edcrfv", nickname="qwertyu",
                                   title="sdfdsffsdfdsf", company="hjkjhliuiytufgfdbv", address="dfgfhtyhjmjh, 567",
                                   home="34564654654654", mobile="34545435345", work="3456467657", fax="76876876867665",
                                   email="qwe@df.io", email2="wsx@ghj.yu", email3="sdsd@fgfhfghfg.edf", homepage="www.fghff.gh",
                                   byear="1980", ayear="2000", address2="dfgdfgfdgfdgrdgrertyfdg, 34342534",
                                   phone2="ertrytryrt", notes="rgfdgfdgtfgthtyhygjyhfth"))
    app.session.logout()
