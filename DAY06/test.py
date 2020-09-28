# test.py
import sqlite3

conn = sqlite3.connect(database='sqlitedb.db')
mycursor = conn.cursor()

try:
    mycursor.execute("drop table sungjuk")
except sqlite3.OperationalError as err:
    print('테이블이 존재하지 않습니다.')

mycursor.execute(
    '''create table sungjuk
    (id text, subject text, jumsu text)''')

datamylist = [('lee', 'java', '10'), ('lee', 'html', '20'), ('lee', 'python', '30')]
sql = "insert into sungjuk(id, subject, jumsu) values(?, ?, ?)"
mycursor.executemany(sql, datamylist)

datamylist = [('jo', 'java', '40'), ('jo', 'java', '50'), ('jo', 'java', '60')]
sql = "insert into sungjuk(id, subject, jumsu) values(?, ?, ?)"
mycursor.executemany(sql, datamylist)

datamylist = [('ko', 'java', '70'), ('ko', 'java', '80'), ('ko', 'java', '90')]
sql = "insert into sungjuk(id, subject, jumsu) values(?, ?, ?)"
mycursor.executemany(sql, datamylist)

conn.commit()

sql = 'select * from sungjuk order by jumsu asc'
for id, subject, jumsu in mycursor.execute(sql):
    print(id + '#' + subject + '#' + jumsu)
print('-' * 30)

mycursor.close()
conn.close()

print('finished')