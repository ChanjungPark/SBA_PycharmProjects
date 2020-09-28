# 20200909.py
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
select * from sungjuk   # 메인 쿼리
where id = (select id from students where name = '이문세');    # 서브 쿼리

고아라의 시험 점수만 출력하기
select jumsu from sungjuk
where id = (select id from students where name = '고아라');
'''