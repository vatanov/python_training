# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.edit_first_contact(Contact(firstname="Edited_qqqqq", middlename="Edited_eeeee", lastname="Edited_aaaaa", nickname="Edited_ffffff",
                                   title="Edited_ccccc", company="Edited_hhhhhhhhh", address="Edited_ddddddddddddd, 999999999",
                                   home="333333333333", mobile="555555555555", work="7777777777", fax="999999999999999",
                                   email="Edited_bbbb@hhhh.oo", email2="Edited_nnn@lll.yy", email3="Edited_pppp@oooo.eee", homepage="www.Editedkkk.hh",
                                   byear="1975", ayear="2015", address2="Edited_jjjjjjjjjjjjjjjjjjjj, 8888888",
                                   phone2="Edited_yyyyyyyyyyyyyyyy", notes="Edited_ff ggggggg ssss kkkkk bbbbbb"))
    app.session.logout()
