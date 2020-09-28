# stringFunction.py
# 문자열 관련 함수 다뤄보기
myString = 'Hello python!'
print('길이 : ', len(myString))
print('포함 개수 : ', myString.count('o'))
print('검색 위치1 : ', myString.find('e'))
print('검색 위치2 : ', myString.find('o', 6))
print('검색 위치3 : ', myString.rfind('o'))   # r : right, l : left -> find는 right에서 하지만 count는 일반 count와 동일

print('문자열 치환1 : ', myString.replace('l', 't'))
print('문자열 치환2 : ', myString.replace('l', 't', 1))
print('문자열 치환3 : ', myString.replace('l', 'blue'))

# sep 옵션은 기본값이 띄어쓰기 입니다.
# 띄어쓰기를 하지 않으려고 sep=''을 사용했습니다.
# strip() 함수는 기본값으로 공백을 제거하는데, 임의의 문자를 내가 지정할 수 있다.
myString = '   가나   다라   '
print('공백 제거1 : [', myString.strip(), ']', sep='')
print('공백 제거2 : [', myString.lstrip(), ']', sep='')
print('공백 제거3 : [', myString.rstrip(), ']', sep='')

myString = 'xxxHello'
print('공백 제거4 : [', myString.strip('x'), ']', sep='')
print('공백 제거5 : [', myString.rstrip('x'), ']', sep='')

myString = 'hello python'
print('대문자 : ', myString.upper())
print('소문자 : ', myString.lower())
print('첫 글자만 대문자 : ', myString.capitalize())

# delimiter : 문자열을 나눠주는 구문자
# split() 함수는 기본값으로 공백을 이용하여 문자를 분리해준다.
print('문자열 분리1 : ', myString.split())

# split() 함수는 사용자가 문자열을 지정하면 지정한 문자를 이용하여 분리해준다.
myString = '소녀시대/빅뱅/원더걸스'
print('문자열 분리2 : ', myString.split('/'))

# startswith('H') : H로 시작하나요?
myString = 'hello_python.xls'
print('시작 여부1 : ', myString.startswith('H'))
print('종료 여부 : ', myString.endswith('.ppt'))

# 메소드 체이닝 : 두개 이상을 쓰는 것
# 대소문자 구분하지 않고, h로 시작합니까?
print('시작 여부2 : ', myString.upper().startswith('H'))
print('시작 여부2 : ', myString.lower().startswith('h'))

myList = ['삼성', '엘지', 'sk']
print('#'.join(myList))

# 인덱싱 : 인덱스를 이용하여 특정 부위의 요소를 1개 추출해내는 것
str = input('문자 입력 : ')    # Korea
pos = 2
munja = str[pos]    # 인덱싱(중요)
print(munja)

# be동사 is로 시작하는 함수들은 참 또는 거짓을 반환해준다.
print('대문자 여부 : ', munja.isupper())
print('소문자 여부 : ', munja.islower())
print('숫자 여부 : ', munja.isdigit())

# 프로그램 내부에서 아스키 코드로 변경이 된 다음, 비교 연산이 이루어진다.
print(munja > 's')  # 'r' > 's' -> 114 > 115
print(munja >= 'A' and munja <= 'Z')
print(munja >= 'a' and munja <= 'z')
print(munja >= '0' and munja <= '9')

# ord() 함수는 문자를 아스키 코드로 바꿔주는 함수이다.
print(ord(munja))
print(ord('A'))
print(ord('a'))
print(ord('0'))