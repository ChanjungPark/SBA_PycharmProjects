# listTest4.py
# list 순서 구조
# 순서를 가지고 있는 데이터 유형
# 인덱싱, 슬라이싱이 가능하고, 대괄호를 사용한다.
# 모든 유형의 데이터 사용이 가능하다.
# 관련 함수 : list()
# 함수들 : len(), append(), insert(), clear()
# sort(). reverse(), remove(), extend(), count(), index()
myList = ['강감찬', '김유신']
print(myList)

myList.append('이순신')
myList.append('안중근')
myList.insert(2, '이성계')
print(myList)
print(len(myList))

# 마지막 요소 구하기
print(myList[len(myList)-1])

# myList.clear()
# print(myList)
# print(len(myList))

myList.sort()
print(myList)

myList.reverse()
print(myList)

# 인덱싱을 이용한 읽기와 쓰기
print(myList[2])    # 읽기
myList[2] = '이완용'   # 쓰기
print(myList)

myList.remove('김유신')
print(myList)

newList = ['윤봉길', '신사임당', '강감찬']
myList.extend(newList)
print(myList)

print(myList.count('강감찬'))

# '이완용'은 몇번째에 있나요? (힌트 : index() 함수 사용)
print('index1 : ', myList.index('이완용'))

print('index2 : ', myList.index('강감찬', 4))

# 슬라이싱 테스트
myLen = len(myList)  # 전체 개수
print(myList[4:6])
print(myList[1::2])
print(myList[1:myLen:2])
print(myList[0::2])
print(myList[0:myLen:2])

# 요소의 인덱스가 3의 배수인 항목들만 추출
print(myList[0:myLen:3])

anyData = [10, '가가', 12.34, [10, 20, 30]]
print(anyData)