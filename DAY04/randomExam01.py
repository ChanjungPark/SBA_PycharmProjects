# randomExam01.py
# 주사위를 10번 던져서 나온 눈의 총합을 구해주는 jusawee 함수를 만들어 보세요.
# 단, 시도 횟수가 입력되지 않으면 5번을 던진다.
import random

def jusawee(n = 5):
    total = 0
    for cnt in range(n):
        x = random.randint(1, 6)
        print('{}번째 나온 눈금 : {}'.format(cnt+1, x))
        total += x
    print('총합 : %d' % total)

sido = 10   # 시도 횟수
jusawee(sido)
print('-' * 30)

jusawee()
print('-' * 30)