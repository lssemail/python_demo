# -*- coding: utf-8 -*-

import uuid

book_id = uuid.uuid1()
now_str = str(book_id).replace('-', '')
print(now_str)