# -*- coding: utf-8 -*-
import sqlite3
import  codecs
db_file = r'C:\Users\vuth1\Documents\Code\onthikithuatvnpt\app\src\main\assets\databases\onthi_full_v2.db'


def open_connection():
    conn = sqlite3.connect(db_file)
    conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
    return conn

def insert_to_db(conn, question, a1, a2, a3,a4, correct_answer, tag_name ):
    tag_id = get_tagid(conn, tag_name)
    if not tag_id:
        print tag_name

    conn.execute("insert into questions (question_text) values (?)",(question,))
    question_id = get_lastest_question_id(conn)
    conn.execute("insert into question_tag (question_id, tag_id) values(?,?)",(question_id, tag_id))
    conn.execute("insert into answers (answer_text) values(?)",(a1,))
    conn.execute("insert into answers (answer_text) values(?)", (a2,))
    conn.execute("insert into answers (answer_text) values(?)", (a3,))
    cursor01 = conn.execute("select answer_id from answers order by answer_id desc limit 3 ")
    index = 3
    for row in cursor01:
        state = 0
        if correct_answer == index:
            state = 1
        id = int(row[0])
        conn.execute("insert into question_answer(question_id, answer_id, state) values(?,?,?)",(question_id, id, state))
        index = index - 1
    if a4:
        state = 0

        conn.execute("insert into answers (answer_text) values(?)", (a4,))
        cursor02 = conn.execute("select max(answer_id) from answers")
        answer_id = 0
        for row in cursor02:
            answer_id = int(row[0])
        if correct_answer == 4:
            state = 1
        conn.execute("insert into question_answer(question_id, answer_id, state) values(?,?,?)",(question_id, answer_id, state))

def get_tagid(conn, tag_name):
    cursor = conn.execute("select tag_id from tags where tag_name=? ", (tag_name,))
    for row in cursor:
        tag_id = int(row[0])
        return tag_id

def get_lastest_question_id(conn):
    cursor00 = conn.execute("select max(question_id) from questions")
    question_id = 0
    for row in cursor00:
        question_id = int(row[0])
    return question_id

