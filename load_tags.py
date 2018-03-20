# -*- coding: utf-8 -*-
import os
import sqlite3
db_file = r'D:\Dropbox\code\android\onthi_v2.db'
list_file = r'C:\Users\vuth1\OneDrive\Documents\On tap Thi Nang luc Ha Tinh 2018 (Moi)\On tap Thi Nang luc Ha Tinh 2018 (Moi)\Vien thong\all'
conn = sqlite3.connect(db_file)
conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
index =0
for list_file in os.listdir(list_file):
    tag_name = list_file.split(r'.')[0]
    conn.execute('insert or ignore into tags(tag_name) values(?)',(tag_name,))

conn.commit()
conn.close()


