# dictControl.py
# 100번 반복한다.
# 매번 1부터 10 사이의 임의의 수를 추출한다.(random 모듈)
# 이것을 사전에 담고, 최종 결과를 출력하도록 한다.('1':2, '2':5, ...)
# list comprehension을 사용하여 리스트로 만든 다음 myList.sort() 함수를 사용하여 정렬하세요.

# 출력 결과 예시
# 숫자1은 12번 추출
# 숫자2는 5번 추출
# ...
# 숫자10은 4번 추출
import random

myDict = {}

for idx in range(1, 101):
    data = random.randint(1, 10)
    if data in myDict:
        myDict[data] += 1
    else:
        myDict[data] = 1

print(myDict)

myList = [key for key in myDict.keys()]
myList.sort()

for key in myList:
    print('숫자 %d는 %d번 추출' % (key, myDict[key]))

print('finished')