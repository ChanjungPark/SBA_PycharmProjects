# starPrint.py
# showStar() 함수를 이용하여 별을 n개 만큼 출력하는 프로그램을 작성하세요.
# 만약 매개변수를 입력하지 않으면 10개를 출력하도록 합니다.

def showStar(n=10):
    if n < 0:
        n = abs(n)

    for i in range(n):
        print('*', end='')
    print()

showStar(5)
print('-' * 30)
showStar()
print('-' * 30)
showStar(30)
print('-' * 30)

for idx in range(1, 11):
    showStar(idx)
print('-' * 30)

showStar(-7)

for item in [3, 5]:
    showStar(item)