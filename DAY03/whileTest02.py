# whileTest02.py
# 무한 whileLoop : 반복 횟수가 몇번인지 모르는 경우
# 어느 조건을 충족하면 반드시 종료해야 합니다.
cnt = 0
while True:
    print('a' + str(cnt))
    cnt += 1
    if cnt == 5:
        break

print('finished')
print('-' * 30)

# 사용자가 입력한 시험 점수에 대한 평균과 개수를 구해봅시다.
# 음수 값이 입력되면 프로그램을 종료하도록 합니다.
sum = 0 # 총점
cnt = 0 # 시험 본 횟수
avg = 0 # 평균

while True:
    score = int(input('점수 입력 : '))
    if score <= 0:
        break
    sum += score
    cnt += 1
    avg = sum/cnt

# print('평균 : %d, 개수 : %d' % (avg, cnt))
print('총 시험 횟수 : {}'.format(cnt))
print('총점 : {}'.format(sum))
print('평균 : {}'.format(avg))