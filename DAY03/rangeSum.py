# rangeSum.py
# 정수 2개를 입력받아서, 앞수에서 뒷수 사이에 있는 모든 정수의 합을 구하세요.
# 앞수 : 2, 뒷수 : 4이면 2 + 3 + 4 = 9 출력
# 앞수 : 5, 뒷수 : 2이면 5 + 4 + 3 + 2 = 14 출력

# 출력 예시 : 2부터 4까지의 총합은 9입니다.
# 만약 절댓값 처리가 필요하면 abs 함수 사용

su1 = int(input('1번째 숫자 입력 : '))    # 앞수
su2 = int(input('2번째 숫자 입력 : '))    # 뒷수

if su1 > su2:
    su1, su2 = su2, su1 # swap

print(su1, '/', su2)

total = 0
for idx in range(su1, su2 + 1):
    total += idx

print('%d부터 %d까지의 총합 : %d' % (su1, su2, total))