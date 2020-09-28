# makeIterable01.py
# Iterable : 반복할 수 있는, 반복 가능한
# list, tuple, dict, 문자열

# list comprehension, set comprehension, dict comprehension
myList01 = [idx for idx in range(1, 5)]
print(myList01)
print('-' * 50)

myList02 = [2 * idx for idx in range(1, 5)]
print(myList02)
print('-' * 50)

# 1, 4, 7, ..., 100
myList03 = [idx for idx in range(1, 101, 3)]
print(myList03)
print('-' * 50)

myList04 = [idx for idx in range(1, 101, 3) if idx%10 == 0]
print(myList04)
print('-' * 50)

# 1부터 10까지의 정수 중에서 3의 배수가 아닌 수들의 총합
# 1 + 2 + 4 + 5 + 7 + 8 + 10 = 37
myList05 = [idx for idx in range(1, 11) if idx%3 != 0]
print(myList05)
print(sum(myList05))
print('-' * 50)

# 중첩 for
myList06 = [x * y for x in range(2, 10) for y in range(1, 10)]
print(myList06)
print('-' * 50)

myList = [('김', 10), ('이', 20), ('최', 30)]

myDict = {data[0]:data[1] for data in myList}
print(myDict)

students = [('이순신', 80, 90), ('김유신', 70, 40)]
# students를 사용하여 다음과 같은 사전을 만들어 보세요.
# '이순신':(80, 90), '김유신':(70, 40)

myDict = {data[0]:data[1] for data in students}
print(myDict)