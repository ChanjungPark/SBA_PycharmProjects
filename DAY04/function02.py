# function02.py
# 두 정수의 합을 구해주는 함수를 구현하고 테스트하세요.
# add(5, 6) -> 11
# add(100, 200) -> 300

def add(x, y):
    return x + y

i = int(input('정수 입력1 : '))
j = int(input('정수 입력2 : '))
result = add(i, j)

print('{}와 {}의 합 : {}'.format(i, j, result))