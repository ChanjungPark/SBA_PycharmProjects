# sqliteEx03.py
'''
조인 : 2개 이상의 테이블을 합쳐서 만드는 새로운 데이터 셋
select 컬럼들
from 테이블A join 테이블 B
on 테이블A.컬럼a = 테이블B.컬럼b;

select *
from students join sungjuk
on students.id = sungjuk.id;

별칭을 사용
select *
from students st join sungjuk sg
on st.id = sg.id;

select st.id, st.name, st.birth, sg.subject, sg.jumsu
from students st join sungjuk sg
on st.id = sg.id;

이름이 '이문세'인 친구의 성적을 구해보자
select id from students where name = '이문세';
select * from sungjuk where id = 'lee';

메인 쿼리 : 외부에 있는 select 구문
서브 쿼리 : 메인 쿼리 내부에 들어있고, 메인 쿼리보다 우선적으로 실행이 되는 쿼리
select * from sungjuk # 메인 쿼리
where id = (select id from students where name = '이문세'); # 서브 쿼리

고아라의 시험 점수만 출력하기
select jumsu from sungjuk
where id = (select id from students where name = '고아라')
'''
import sqlite3

class SqliteDB:
    def __init__(self, dbname):
        print('생성자 출력')
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()

    def __del__(self):  # 소멸자(마감 처리 용도)
        print('소멸자 출력')
        self.cursor.close()
        self.conn.close()

    def getJoinData(self):  # 조인 데이터
        sql = " select st.id, st.name, st.birth, sg.subject, sg.jumsu"
        sql += " from students st join sungjuk sg"
        sql += " on st.id = sg.id"

        result = self.cursor.execute(sql)
        return result

    def getSubQuery(self, name):
        sql = " select * from sungjuk"
        sql += " where id = (select id from students where name = '%s')"

        result = self.cursor.execute(sql % (name))
        return result

    def getJumsu(self, name):
        sql = " select jumsu from sungjuk"
        sql += " where id = (select id from students where name = '%s')"

        mydata = self.cursor.execute(sql % (name))

        total = 0   # 총점
        cnt = 0 # 행 개수

        for row in mydata:
            total += row[0]
            cnt += 1

        if cnt == 0:
            return None # 부정(negative)

        avg = total / cnt

        return (total, avg)

        '''
        if dataset != None:
            avg = total / cnt
            print('총점 : ', dataset[0])
            print('평균 : ', dataset[1])
            return (total, avg)
        else:
            print('존재하지 않는 회원입니다.')
            return None
        '''

dbname = 'sqlitedb.db'
mydb = SqliteDB(dbname)

dataset = mydb.getJoinData()
for row in dataset:
    print(row)
print('#' * 50)

who = '이문세'
dataset = mydb.getSubQuery(who)
for (id, subject, jumsu) in dataset:
    print('아이디 :', id, end='', sep='')
    print(', 과목 :', subject, end='', sep='')
    print(', 점수 :', jumsu, end='', sep='')
    print()
print('#' * 50)

# 고아라, 심형래 구현해 보세요.
who = '고아라'
dataset = mydb.getJumsu(who)
print('총점 :', dataset[0])
print('평균 :', dataset[1])
print('#' * 50)

who = '심형래'
dataset = mydb.getJumsu(who)

if dataset != None:
    print('총점 : ', dataset[0])
    print('평균 : ', dataset[1])
else:
    print('존재하지 않는 회원입니다.')
print('#' * 50)

print('finished')