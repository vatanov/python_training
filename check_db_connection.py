from fixture.orm import ORMFixture
from fixture.db import DbFixture
import random
import re

# db = ORMFixture(host="127.0.0.1", name = "addressbook", user="root", password="")
#
# try:
#     l = db.get_group_list()
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass #db.destroy()



db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
if len(db.get_group_list()) > 0:
    random_group = random.choice(db.get_group_ids())
    group_id = int(re.sub("[(),]", "", random_group.id))
    print(group_id)
else:
    group_id = 0
    print(group_id)
