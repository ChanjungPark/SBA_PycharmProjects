# myDeviation.py
# 표준 편차 구하기
'''
1) 평균을 구합니다.
평균 = 총합(160)/요소 개수 = 160/4 = 40

2) (점수 - 평균)의 제곱을 모두 누적시킵니다.
900 + 100 + 0 + 1600 = 2600

3) 2의 결과에 돗수를 나눕니다.
2600/요소 개수 = 2600/4 = 650

4) 3의 결과에 루트를 씌웁니다.
루트 650 = 25.4950975

힌트 : sqrt(650)
루트는 외부 모듈인 math 모듈의 sqrt를 사용하면 됩니다.
'''
import math # 수학과 관련된 모듈

print(math.sqrt(650))
print(math.sqrt(4))
print('-' * 30)

# 내가 작성한 함수
def deviation01(myList):
    sum = avg = 0
    for i in range(0, len(myList)):
        sum += myList[i]
    avg = sum/len(myList)

    x = y = 0
    xSum = 0
    for j in range(0, len(myList)):
        x = (myList[j] - sum) ** 2
        xSum += x
    y = xSum/len(myList)

    return math.sqrt(y)

# 강사님이 작성한 함수
def deviation02(myList):
    length = len(myList)
    total = 0.0
    for item in myList:
        total += item
    average = total / length

    imsi = 0.0
    for item in myList:
        imsi += (average - item) ** 2
    imsi  = imsi / length

    return math.sqrt(imsi)

# 다음 리스트를 이용하여 표준 편차를 구해주는 함수 deviation을 구현해보세요.
myList = [10, 20, 30, 40]
result = deviation01(myList)
print('표준 편차 :', result)
print('-' * 30)

result = deviation02(myList)
print('표준 편차 :', result)
print('-' * 30)