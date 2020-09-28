# updownTest.py
# 모듈을 사용하고자 할 때 import 키워드를 사용하면 됩니다.
# random 모듈 : 랜덤한 데이터를 추출하고자 할 때 사용하는 모듈
import random
# for idx in range(1, 11):
#     answer = random.randint(1, 100)
#     print(answer)
# print('finished')

answer = random.randint(1, 100) # answer : 컴퓨터가 기억한 값
# print('정답 : %d' % (answer))

cnt = 0 # 시도 횟수

while True:
    su = int(input('1부터 100사이의 정수 1개 입력 : '))   # 우리가 입력한 숫자
    cnt += 1    # 시도 횟수를 1 증가
    if su < answer:
        # pass
        print('%d보다 큰 수를 입력하세요.' % (su))
    elif su > answer :
        # pass
        print('%d보다 작은 수를 입력하세요.' % (su))
    else :
        # pass
        print('정답입니다.')
        print('%d번만에 맞췄습니다.' % (cnt))
        break

print('finished')