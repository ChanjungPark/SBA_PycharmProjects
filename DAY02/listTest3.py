# listTest3.py
# 중첩 리스트
# 중첩된 개수만큼 대괄호를 사용하면 됩니다.
saram01 = ['hong', '홍길동', 20, '용산']
saram02 = ['kim', '김철수', 30, '마포']
saram03 = ['kang', '강남', 40, '구로']

myList = []
myList.append(saram01)
myList.append(saram02)
myList.append(saram03)
print(myList)

print(myList[1][2])
myList[2][1] = '강호동'
print(myList)

# 세사람의 평균 나이 구하기
myLen = len(myList)
sum = myList[0][2] + myList[1][2] + myList[2][2]
print('평균 나이 : %.2f' % (sum/myLen))

# '홍길동$김철수$강호동' 출력해보기 (힌트 : join() 함수)
newList = [myList[0][1], myList[1][1], myList[2][1]]
print('$'.join(newList))