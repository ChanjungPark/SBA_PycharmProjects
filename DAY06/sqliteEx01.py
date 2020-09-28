# sqliteEx01.py
'''
sql : ddl + dql + dml + tcl + etc

ddl(데이터 정의어) : create

create table : 테이블 생성 구문
students 테이블 : 2차원의 형식의 표
3개의 컬럼을 가지고 있습니다.(문자는 text, 숫자는 integer)
create table students(id text primary key, name text, birth text);
commit;

primary key : 필수이면서 동시에 같은 값을 가질 수 없는 컬럼

주의
문자열이나 날짜 형은 반드시 외따옴표를 넣어줘야 한다.
행 추가, 수정, 삭제 등은 반드시 커밋을 해줘야 한다.
커밋(commit)이란 데이터베이스에서 영구적으로 저장하는 동작을 의미합니다.

dml(데이터 조작어) 구문 : insert, update, delete

행 추가
insert into students(id, name, birth) values('lee', '이승기', '1998/12/25');
insert into students(id, name, birth) values('kang', '강감찬', '1111/11/11');
lee, 이승기, 1989/12/25
kang, 강감찬, 1111/11/11
commit ;

행 정보 수정
update students set name = '이순신' where id = 'lee';
commit;

# 강감찬의 생일을 1000/10/10으로 변경하새보세요.
update students set birth = '1000/10/10' where id = 'kang';
commit;

모든 행 삭제
delete from students;
commit;

트랜잭션(tcl) : coomit <-> rollback
commit;

데이터 제거하기
drop table students;

dql(데이터 질의어) : select

모든 데이터를 조회하는 문장
select * from students;

id가 'ko'인 학생을 조회하는 구문
select * from students where id = 'ko';

order by : 정렬하는 것(asc : 오름차순, desc : 내림차순)
select * from students order by name desc;

like 연산자 : whidcard를 사용한 조회
whidcard 문자
_(언더바)는 1글자를 의미
%는 0개 이상 무한개 이하를 의미

이% : 성씨가 '이'씨인 사람
%이 : 이름의 끝이 '이'로 끝나는 사람
%이% : 이름 가운데 '이'가 들어있는 사람

select * from students where name like '%이%';

fetch(패치) :내용물의 요소를 바깥으로 끄집어 내는 동작
    fetch_one(), fetch_all()
'''
# sqlite : 소형 개인용 데이터 저장을 위한 데이터베이스
import sqlite3  # sqlite를 위한 모듈

# conn : 데이터베이스에 접근하기 위한 객체
# database : 데이터베이스 파일 이름
conn = sqlite3.connect(database='sqlitedb.db')
print(type(conn))

# cursor(커서) : 데이터베이스 작업을 수행하고 있는 메모리 공간
mycursor = conn.cursor()

# sqlite3.OperationalError: no such table: students
# mycursor.execute("drop table students")

try:
    # execute : sql 구문을 실행해주는 함수
    mycursor.execute("drop table students")
except sqlite3.OperationalError as err:
    print('테이블이 존재하지 않습니다.')

mycursor.execute(
    '''create table students
    (id text primary key, name text, birth text)''')

sql = "insert into students(id, name, birth) values('lee', '이승기', '1998/12/25')"
mycursor.execute(sql)

sql = "insert into students(id, name, birth) values('kang', '강감찬', '1111/11/11')"
mycursor.execute(sql)

datamylist = [('jo', '조용필', '1985/12/31'), ('ko', '고아라', '1970/07/17'), ('sim', '심형래', '1950/06/06')]

# ?를 place holder라고 하는데, 치환되어야 할 어떠한 대상
# 데이터 유형에 상관없이 외따옴표 적지 마라
sql = "insert into students(id, name, birth) values(?, ?, ?)"
# mycursor.executemany(sql=sql, seq_of_parameters=datamylist)
mycursor.executemany(sql, datamylist)

conn.commit()

# findID = 'ko'
findID = 'ko2222'   # TypeError: 'NoneType' object is not subscriptable
sql = "select * from students where id = '%s'"

mycursor.execute(sql % (findID))

result = mycursor.fetchone()
print(type(result))
if result != None:
    print('아이디 : ' + result[0], end='')
    print(', 이름 : ' + result[1], end='')
    print(', 생일 : ' + result[2], end='')
    print()
else:
    print('문제가 있습니다.')
print('-' * 30)

# asc는 명시하지 않아도 됨
sql = 'select * from students order by name desc'   # asc <-> desc
# for row in mycursor.execute(sql):
for id, name, birth in mycursor.execute(sql):
    # print(row)
    print(id + '#' + name + '#' + birth)
print('-' * 30)

sql = "select * from students where name like '%이%'"
mycursor.execute(sql)
print(mycursor.fetchall())
print('-' * 30)

# 'id'가 lee인 친구의 이름을 '이문세'로 바꾸세요
# sql = "update students set name = '이문세' where id = 'lee'"
# mycursor.execute(sql)
pid = 'lee'
newname = '이문세'
sql = "update students set name = '%s' where id = '%s'"
mycursor.execute(sql % (newname, pid))

# 'id'가 sim인 친구의 데이터를 삭제하세요.
# sql = "delete from students where id = 'sim'"
# mycursor.execute(sql)
pid = 'sim'
sql = "delete from students where id = '%s'"
mycursor.execute(sql % (pid))

conn.commit()

sql = 'select * from students order by name asc'
for id, name, birth in mycursor.execute(sql):
    print(id + '#' + name + '#' + birth)
print('-' * 30)

mycursor.close()
conn.close()

print('finished')