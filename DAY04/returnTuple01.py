# returnTuple01.py
# 튜플을 사용하여 반환되는 데이터를 여러개 만들기
def myFunc(x, y):
    if y == 0:
        temp = x
    else:
        temp = x//y

    return x+y, x-y, x*y, temp

su1 = 14
su2 = 0
result = myFunc(su1, su2)
print(result)
print('-' * 30)

su1 = 14
su2 = 5
result = myFunc(su1, su2)
print(result)
print('-' * 30)

# 리스트의 모든 요소의 절댓값을 구하고,
# 최대(max), 최소(min), 총합(sum), 평균(avg)을 튜플로 반화하세요.
def myFunc2(myList):
    newList = [abs(item) for item in myList]
    myMax = max(newList)
    myMin = min(newList)
    mySum = sum(newList)
    myAvg = mySum/len(newList)
    return myMax, myMin, mySum, myAvg

myList = [10, -20, 30, -50, 40]
result = myFunc2(myList)
print(result)
print('-' * 30)