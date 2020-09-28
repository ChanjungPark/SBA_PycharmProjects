# whileTest01.py
# 숫자 5를 입력받고, 5단 출력하기
# 5 * 1 = 5
# 5 * 2 = 5
# 음수를 입력받으면, 절댓값으로 변경하여 출력하기
dan = int(input('몇 단 출력 : '))
i = 1

while i < 10:
    if dan < 0:
        dan = abs(dan)
    myString = '%d * %d = %d' % (dan, i, dan*i)
    print(myString)
    i += 1
print('finished')