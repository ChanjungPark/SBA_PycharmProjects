# function05.py
# 함수의 마지막에는 return 구문이 들어갑니다.
# 만약 명시하지 않으면 return None 라는 구문이 숨어 있습니다.

# None : 리턴하지 않는, 의미가 없는
# void, vacant, empty, no response
def namePrint(name, age):
    print('{}님의 나이는 {}살 입니다.'.format(name, age))
    return None

name = '제시카'
age = 20
result = namePrint(name, age)
print(result)

if result == None:
    print('데이터를 구하지 못했습니다.')
else:
    print('참 잘했어요.')

print('-' * 30)

def gugudan(x):
    n = range(1, 10)    # 1부터 9까지
    for y in n:
        print('{} * {} = {}'.format(x, y, x*y))

dan = 3
gugudan(dan)
print('-' * 30)

# 2, 4, 7단을 출력해보세요.
myList = [2, 4, 7]
for i in range(0, len(myList)):
    gugudan(myList[i])
    print('-' * 30)

# 2단이면 [2, 4, 6, ..., 18] 출력되는 함수를 만들어 보세요.
def gugu(n):
    result = [n*idx for idx in range(1, 10)]
    print(result)

su = 2
print(gugu(su))
print('-' * 30)

# 2단부터 4단까지 각 단의 결과를 list 형식으로 출력해보세요.
def gu(x, y):
    for i in range(x, y+1):
        result = [i*idx for idx in range(1, 10)]
        print(result)
        print('-' * 30)

x, y = 2, 4
print(gu(x, y))