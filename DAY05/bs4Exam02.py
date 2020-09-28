# bs4Exam02.py
# 카페 첨부파일에서 첨부(2주차).zip, 파이썬 Konpy 설정하기.txt 다운로드하기
# 첨부(2주차).zip 압축 해제하고, 파일 추가(drag & drop)
# 참조 파일(fruits.html)을 이용하여 필요한 정보를 추출해보도록 합니다.
# BeautifulSoup 패키지 : html 문서에서 데이터를 추출하고자 할 때 사용하는 패키지
from bs4 import BeautifulSoup
# open 함수 : 운영체제 내의 파일을 열고자 할 때 사용하는 내장 함수
# 파일 이름 : 'fruits.html'. 'r'은 read(읽기)
html = open('fruits.html', 'r', encoding='utf-8')   # fruits.html

# 파서(parser) : html 문서가 제대로 잘 만들어진 것인지를 검증하는 객체
# soup = BeautifulSoup(해당문서, '파싱문자열')
soup = BeautifulSoup(html, 'html.parser')
# print(type(soup))

body = soup.select_one('body')  # html 문서 안의 body가 하나일때는 select_one
ptag = body.find('p')

# 읽기
print(ptag) # p 태그
print(ptag['class'])    # class 속성
print(ptag['align'])    # align 속성
print('-' * 60)

# 쓰기
# print(ptag['id'])   # KeyError: 'id'
ptag['id'] = 'apple'
print(ptag['id'])
print(ptag)
print('-' * 60)

body_tag = soup.find('body')
print(body_tag)
print('-' * 60)

# print(body_tag.children)
# print('-' * 60)

idx = 0
# white character : 눈에 보이지 않는 글자들
for child in body_tag.children:
    idx += 1
    print(str(idx) + '번째 요소 :', child)
    print('#' * 60)
    print('a')
print('-' * 60)

myDiv = soup.find('div')
print(myDiv)
print('-' * 60)
print('나의 부모는')
print(myDiv.parent)
print('-' * 60)

# attrs 매개 변수는 속성(attribute)을 찾고자 할 때 사용합니다.
myTag = soup.find('p', attrs={'class':'hard'})
print(myTag)
print('-' * 60)

print(myTag.find_parent())
print('-' * 60)

print('myTag 태그 모든 상위 부모 태그들의 이름')
parents = myTag.find_parent()
for p in parents:
    print(p.name)