# -*- coding: utf-8 -*-
from model.contact import Contact


testdata = [Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", nickname="nickname1",
                    title="title1", company="company1", address="address1", home="111", mobile="222", work="333",
                    fax="444", email="email1_1", email2="email2_1", email3="email3_1", homepage="homepage1", bday="3",
                    bmonth="3", byear="1975", aday="4", amonth="4", ayear="1985", address2="address2_1", phone2="555",
                    notes="notes_1"),
            Contact(firstname="firstname2", middlename="middlename2", lastname="lastname2", nickname="nickname2",
                    title="title2", company="company2", address="address2", home="777", mobile="888", work="999",
                    fax="000", email="email1_2", email2="email2_2", email3="email3_2", homepage="homepage2", bday="6",
                    bmonth="6", byear="1990", aday="8", amonth="5", ayear="2004", address2="address2_2", phone2="221",
                    notes="notes_2")]