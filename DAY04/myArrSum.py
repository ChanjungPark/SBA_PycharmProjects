# myArrSum.py
# 리스트의 모든 요소들의 합을 구해주는 함수 arrSum을 만들어 보세요.
def arrSum(list01):
    total = 0
    for item in list01:
        total += item
    return total

myList = [10, 20, 30, 40]   # 리스트
result = arrSum(myList)
print(result)
print('-' * 30)

myTuple = (1, 2, 3)  # 튜플
result = arrSum(myTuple)
print(result)
print('-' * 30)

# 집합을 이용하여 테스트 요망
mySet = set((11, 22, 33))
result = arrSum(mySet)
print(result)
print('-' * 30)